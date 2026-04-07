import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    e_x = np.exp(x)
    e_minus_x = np.exp(-x)
    
    return (e_x - e_minus_x) / (e_x + e_minus_x)