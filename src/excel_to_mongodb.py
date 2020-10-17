import pandas as pd
import config
import utils

def read_excel_data(filepath):
    """Reads Excel file and returns Pandas DataFrame of the same"""
    return pd.read_excel(filepath)

def get_list_of_excel_posts():
    """
    Extracts posts from the given Excel spreadsheet.
    Returns list of dictionaries containing the posts to be added to a collection in the MongoDB database.
    NOTE: Adds an additional "_id" (will be unique field) key in each dictionary.
    """
    posts = []
    df = read_excel_data(filepath=config.EXCEL_FILEPATH)
    for tuple_obj in df.itertuples():
        post = {
            "_id": utils.generate_random_id(),
            "id": tuple_obj.id,
            "quote": tuple_obj.quotes,
            "author": tuple_obj.author,
            "source": tuple_obj.source,
            "rating": tuple_obj.rating,
            "addedBy": tuple_obj.addedBy,
        }
        posts.append(post)
    return posts

def add_excel_posts_to_mongodb(collection_name):
    """Adds posts from Excel spreadsheet into MongoDB database"""
    posts = get_list_of_excel_posts()
    collection = utils.get_collection_object(collection_name=collection_name)
    collection.insert_many(posts)
    return None

if __name__ == "__main__":
    # Deleting posts from same collection before adding from Excel sheet, just in case
    utils.delete_posts_from_mongodb(collection_name=config.MONGODB_COLLECTION_NAME)
    add_excel_posts_to_mongodb(collection_name=config.MONGODB_COLLECTION_NAME)
    print("Successfully added posts from Excel spreadsheet to MongoDB database!")