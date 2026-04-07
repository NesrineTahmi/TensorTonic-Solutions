import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.array(x, dtype=float)
    
    def gelu_scalar(val):
        erf_val = math.erf(val / math.sqrt(2))
        return 0.5 * val * (1 + erf_val)

    v_gelu = np.vectorize(gelu_scalar)

    return v_gelu(x)