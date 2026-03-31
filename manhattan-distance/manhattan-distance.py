import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    if (len(x) != len(y)):
        raise ValueError("x and y have different dimensions !")

    
    distance = 0.0
    
    x = np.array(x)
    y = np.array(y)

    for i in range(len(x)):
        distance += np.abs(x[i]- y[i])

    return distance