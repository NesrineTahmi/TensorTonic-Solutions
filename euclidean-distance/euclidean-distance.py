import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    distance = 0
    n = len(x)
    if len(x) != len(y):
        raise ValueError("x and y do not have the same size !")

    x = np.array(x)
    y = np.array(y)

    
    for i in range(n):
        distance += np.square(x[i] - y[i])

    return np.sqrt(distance)
    