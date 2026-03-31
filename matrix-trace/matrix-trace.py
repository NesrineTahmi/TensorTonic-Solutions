import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    n = len(A)
    m = len(A[0])

    if n != m :
        raise ValueError("Matrix must be square")

    trace = 0.0

    for i in range(n):
        trace += A[i][i]

    return trace
