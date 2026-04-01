import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.array([])
    
    if max_len is None:
        leng = []
        for seq in seqs:
            leng.append(len(seq))
        max_len = max(leng) if leng else 0

    result_pad = np.full((len(seqs), max_len), pad_value)

    for i, seq in enumerate(seqs):
        content = seq[:max_len]
        result_pad[i, :len(content)] = content
        

    return result_pad
            