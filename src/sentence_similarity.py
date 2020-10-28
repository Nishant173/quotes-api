import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_cosine_similarity(doc1, doc2):
    """
    Gets cosine similarity score (float) between two given documents.
    Cosine similarity is a number (float) between [0, 1]. The closer it is to 1, higher the similarity
    between the two documents given.
    """
    count_vectorizer = CountVectorizer(stop_words='english')
    sparse_matrix = count_vectorizer.fit_transform(raw_documents=[doc1, doc2])
    dtm = sparse_matrix.todense()
    df_dtm = pd.DataFrame(data=dtm, 
                          columns=count_vectorizer.get_feature_names(), 
                          index=['doc1', 'doc2'])
    similarity_matrix = cosine_similarity(df_dtm, df_dtm)
    similarity_score = round(similarity_matrix[0][1], 6)
    return similarity_score