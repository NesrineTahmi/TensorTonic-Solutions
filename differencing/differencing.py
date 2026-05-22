def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    if len(series) < order + 1:
        return

    result = series.copy()
    for i in range(order):
        
        for j in range(len(result)-1):
            result[j] = result[j+1] - result[j]
        result = result[:-1]
        
    return result