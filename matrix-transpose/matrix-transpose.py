import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n = len(A[0]) 
    m = len(A) 
    if n < 1 or m > 1000:
        return
        
    T_A = np.zeros((n, m)) 

    for i in range(n):
        for j in range(m):
            T_A[i][j] = A[j][i]
    print(T_A)

    return T_A
