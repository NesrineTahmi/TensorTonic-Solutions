import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    vocab_arr = np.array(vocab)
    
    bow_vect = np.zeros(len(vocab), dtype=int)

    for token in tokens:
        mask = (vocab_arr == token)
        bow_vect += mask.astype(int)
        
    return bow_vect