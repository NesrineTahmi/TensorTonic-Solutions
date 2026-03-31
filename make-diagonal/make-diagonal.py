import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    
    n = len(v)
    v = np.array(v)
    diag = np.zeros((n,n))
    
    for i in range(n):
        diag[i][i] = v[i]

    return diag
