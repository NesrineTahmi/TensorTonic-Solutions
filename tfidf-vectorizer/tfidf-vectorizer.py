import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    
    # Write code here
    all_words = []
    tokenized_docs = []
    for doc in documents:
        tokens = doc.lower().split()
        all_words.extend(tokens)
        tokenized_docs.append(tokens)

    vocabulary = sorted(list(set(all_words)))
    
    n = len(documents)
    m = len(vocabulary)

    tfidf_matrix = np.zeros((n, m)) 

    for i in range(n):
        current_doc = tokenized_docs[i]
        for j in range(m):
            current_term = vocabulary[j]
            total_count = current_doc.count(current_term)
            tf = total_count / len(current_doc)

            count = 0
            for doc in tokenized_docs:
                if current_term in doc:
                    count += 1
            idf = math.log(n / count)

            tfidf_matrix[i, j] = tf * idf

    return tfidf_matrix, vocabulary
            