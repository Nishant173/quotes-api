import random
from pymongo import MongoClient
import config

def generate_random_id():
    """Returns random 12 digit ID (str)"""
    random_id = ""
    characters = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for _ in range(12):
        random_id += random.choice(characters)
    return random_id

def get_collection_object(collection_name):
    """Returns object of the collection instance from the MongoDB database"""
    cluster = MongoClient(config.MONGODB_CONNECTION_URI)
    db = cluster[config.MONGODB_DB_NAME]
    collection_obj = db[collection_name]
    return collection_obj

def get_all_posts_from_mongodb(collection_name):
    """Returns list of all posts in a collection from the MongoDB database"""
    collection = get_collection_object(collection_name=collection_name)
    all_posts = list(collection.find({}))
    return all_posts

def delete_posts_from_mongodb(collection_name):
    """Deletes all posts from a collection in the MongoDB database"""
    collection = get_collection_object(collection_name=collection_name)
    collection.delete_many({})
    return None