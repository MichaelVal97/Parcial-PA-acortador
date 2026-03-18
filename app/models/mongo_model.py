from app import mongo

def save_image(short_code, image_url):
    collection = mongo.images
    collection.insert_one({
        "short_code": short_code,
        "image_url": image_url
    })

def get_image(short_code):
    collection = mongo.images
    return collection.find_one({"short_code": short_code})