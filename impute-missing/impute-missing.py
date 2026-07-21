import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    X_imputed = np.array(X, dtype=float).copy()
    
    #edge case 1d array
    is_1d = X_imputed.ndim == 1
    if is_1d:
        X_imputed = X_imputed.reshape(-1, 1)
        
    stat_func = np.nanmean if strategy == 'mean' else np.nanmedian
    
    for col in range(X_imputed.shape[1]):
        col_data = X_imputed[:, col]
        nan_mask = np.isnan(col_data)
        
        if nan_mask.any():
            #if the whole column is NaN, default to 0.0, we cant calculate anything
            if nan_mask.all():
                stat_val = 0.0
            else:
                stat_val = stat_func(col_data)
                
            col_data[nan_mask] = stat_val

    if is_1d:
        X_imputed = X_imputed.ravel()
        
    return X_imputed