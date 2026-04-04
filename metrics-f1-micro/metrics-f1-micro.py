import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    if (len(y_pred) != len(y_true)):
        raise ValueError("Different array sizes.")

    if len(y_pred) == 0:
        return 0.0
        
    tp = np.sum(y_pred == y_true)
    fn_fp = np.sum(y_pred != y_true)
    fn = fn_fp
    fp = fn_fp

    return (2*tp) / (2*tp + fn + fp)