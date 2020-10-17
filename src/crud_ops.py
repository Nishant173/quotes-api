import numpy as np
import utils

def add_quote(quote, collection_name):
    """Adds one quote to a collection in the MongoDB database"""
    collection = utils.get_collection_object(collection_name=collection_name)
    obj_to_add = {
        "_id": utils.generate_random_id(),
        "id": "",
        "quote": quote,
        "author": "",
        "source": "",
        "rating": np.nan,
        "addedBy": "",
    }
    collection.insert_one(obj_to_add)
    return None

def delete_quote(quote_id, collection_name):
    """Deletes one quote from a collection (based on _id) in the MongoDB database"""
    collection = utils.get_collection_object(collection_name=collection_name)
    collection.delete_one({"_id": quote_id})
    return None

def update_quote_rating(quote_id, new_rating, collection_name):
    """Updates rating of one quote from a collection in the MongoDB database"""
    collection = utils.get_collection_object(collection_name=collection_name)
    collection.update_one(filter={"_id": quote_id},
                          update={"$set": {"rating": new_rating}})
    return None