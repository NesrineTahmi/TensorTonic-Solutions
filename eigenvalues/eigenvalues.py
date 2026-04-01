import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    if matrix is None or len(matrix) == 0:
        return None

    num_rows = len(matrix)

    for row in matrix:
        try:
            if len(row) != num_rows:
                return None
        except TypeError: 
            return None
 

    return np.linalg.eigvals(matrix)