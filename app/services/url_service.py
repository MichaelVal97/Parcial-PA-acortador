import random
import string
from app.models.mysql_model import *
from app.models.mongo_model import *

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_short_url(original_url, image_url, description):
    # Validar duplicado
    existing = get_by_original(original_url)
    if existing:
        return existing["short_code"]

    # Generar código único
    while True:
        code = generate_code()
        if not get_by_code(code):
            break

    # Guardar en MySQL
    insert_url(original_url, code, description)

    # Guardar en Mongo
    save_image(code, image_url)

    return code