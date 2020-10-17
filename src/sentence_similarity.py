from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def get_cosine_similarity(sentence1, sentence2):
    """
    Calculates and returns cosine similarity (float) of 2 sentences.
    Cosine similarity is a float between [0, 1]. The closer it is to 1, higher the similarity
    between the 2 sentences given.
    """
    stop_words = stopwords.words('english')
    sent1_tokenized = word_tokenize(text=sentence1)
    sent2_tokenized = word_tokenize(text=sentence2)
    sent1_set = set([word for word in sent1_tokenized if word not in stop_words])
    sent2_set = set([word for word in sent2_tokenized if word not in stop_words])
    rvector = sent1_set.union(sent2_set)
    list1 = []
    list2 = []
    for word in rvector:
        if word in sent1_set:
            list1.append(1)
        else:
            list1.append(0)
        if word in sent2_set:
            list2.append(1)
        else:
            list2.append(0)
    sum_ = 0
    for i in range(len(rvector)):
        sum_ += list1[i] * list2[i]
    cosine_similarity = sum_ / float((sum(list1) * sum(list2)) ** 0.5)
    return round(cosine_similarity, 6)