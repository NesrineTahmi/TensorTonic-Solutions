import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    matrix = np.array(matrix, dtype=float)
    denom = 1

    if matrix.ndim != 2 or axis not in (0,1, None): #1D matrix
        return None
    
    if norm_type == 'l1' :
        denom = np.sum(np.abs(matrix), axis= axis, keepdims=True)
    elif norm_type == 'l2' :
        denom = np.sqrt(np.sum(np.square(matrix), axis=axis, keepdims=True))
    elif norm_type == 'max' :
        denom = np.max(matrix, axis=axis, keepdims=True)
    else:
        return None
        
    denom = np.where(denom == 0, 1, denom)
    
    return matrix /denom