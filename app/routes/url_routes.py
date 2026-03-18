from flask import Blueprint, render_template, request, redirect
from app.services.url_service import create_short_url
from app.models.mysql_model import get_by_code, get_all
from app.models.mongo_model import get_image

url_bp = Blueprint("url_bp", __name__)

@url_bp.route("/", methods=["GET", "POST"])
def index():
    short_url = None

    if request.method == "POST":
        original = request.form["original_url"]
        image = request.form["image_url"]
        desc = request.form["description"]

        code = create_short_url(original, image, desc)
        short_url = request.host_url + code

    return render_template("index.html", short_url=short_url)


@url_bp.route("/history")
def history():
    urls = get_all()

    data = []
    for u in urls:
        img = get_image(u["short_code"])
        data.append({
            **u,
            "image": img["image_url"] if img else ""
        })

    return render_template("history.html", urls=data)


@url_bp.route("/<code>")
def redirect_url(code):
    url = get_by_code(code)

    if url:
        return redirect(url["original_url"])

    return "URL no encontrada", 404