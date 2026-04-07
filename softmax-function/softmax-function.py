import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x  = np.array(x, dtype=float)

    if x.ndim == 1:
        axis = 0
    else:
        axis = 1
    
    max  = np.max(x, axis, keepdims=True)
    exp = np.exp(x - max)

    sum = np.sum(exp, axis, keepdims=True)
    
    return exp / sum