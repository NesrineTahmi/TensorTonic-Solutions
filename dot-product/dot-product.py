import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    dot = 0
    n = len(x)
    if len(x) != len(y):
        raise ValueError("x and y do not have the same size !")
    
    for i in range(n):
        dot += x[i]*y[i]
    return dot