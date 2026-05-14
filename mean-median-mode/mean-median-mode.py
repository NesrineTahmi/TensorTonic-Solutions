import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """

    values, counts = np.unique(x, return_counts=True)

    index = np.argmax(counts)
    mode = values[index]

    
    return (float(np.mean(x)), float(np.median(x)), float(mode))