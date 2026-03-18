from flask import Flask
from app.config import Config
from pymongo import MongoClient
import pymysql

mongo = None
mysql = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    global mongo, mysql

    # MongoDB
    mongo = MongoClient(app.config["MONGO_URI"])[app.config["MONGO_DB"]]

    # MySQL
    mysql = pymysql.connect(
        host=app.config["MYSQL_HOST"],
        user=app.config["MYSQL_USER"],
        password=app.config["MYSQL_PASSWORD"],
        database=app.config["MYSQL_DB"],
        cursorclass=pymysql.cursors.DictCursor
    )

    from app.routes.url_routes import url_bp
    app.register_blueprint(url_bp)

    return app