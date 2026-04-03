import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    if not np.isclose(np.sum(p), 1.0):
        raise ValueError("Probabilities do not add up to 1.")

    
    return float(np.dot(x, p))
