import pandas as pd
import config
from sentence_similarity import get_cosine_similarity
import utils

def get_quote_by_id(quote_id):
    """Gets one quote based on ID (if it exists); otherwise returns empty dictionary"""
    all_posts = utils.get_all_posts_from_mongodb(collection_name=config.MONGODB_COLLECTION_QUOTES)
    df_all_posts = pd.DataFrame(data=all_posts)
    df_post_by_id = df_all_posts[df_all_posts['_id'] == quote_id]
    if len(df_post_by_id) == 1:
        return df_post_by_id.to_dict(orient='records')[0]
    return {}

def get_rated_posts():
    all_posts = utils.get_all_posts_from_mongodb(collection_name=config.MONGODB_COLLECTION_QUOTES)
    df_all_posts = pd.DataFrame(data=all_posts)
    df_rated_posts = df_all_posts[df_all_posts['rating'].notna()]
    return df_rated_posts.to_dict(orient='records')

def get_unrated_posts():
    all_posts = utils.get_all_posts_from_mongodb(collection_name=config.MONGODB_COLLECTION_QUOTES)
    df_all_posts = pd.DataFrame(data=all_posts)
    df_unrated_posts = df_all_posts[df_all_posts['rating'].isna()]
    return df_unrated_posts.to_dict(orient='records')

def get_recommended_posts():
    all_posts = utils.get_all_posts_from_mongodb(collection_name=config.MONGODB_COLLECTION_QUOTES)
    df_all_posts = pd.DataFrame(data=all_posts)
    df_recommended_posts = df_all_posts[df_all_posts['rating'] > 3]
    return df_recommended_posts.to_dict(orient='records')

def get_similar_quotes(quote, top):
    """Gets list of most similar quotes available (from recommended quotes collection)"""
    recommended_posts_with_similarities = []
    recommended_posts = get_recommended_posts()
    for post in recommended_posts:
        post['cosineSimilarity'] = get_cosine_similarity(sentence1=quote, sentence2=post['quote'])
        recommended_posts_with_similarities.append(post)
    df_similarities = pd.DataFrame(data=recommended_posts_with_similarities)
    df_similarities.sort_values(by='cosineSimilarity', ascending=False, ignore_index=True, inplace=True)
    df_similarities = df_similarities.head(top)
    return df_similarities.to_dict(orient='records')