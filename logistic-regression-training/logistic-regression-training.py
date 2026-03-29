import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    
    n, m = X.shape
    w = np.zeros(m)
    b = 0.0
 
    for i in range(steps):
        z = np.dot(X, w) + b
        p = _sigmoid(z)
        
        dL_dw = (1/n) * np.dot(X.T, (p - y))
        dL_db = (1/n) * np.sum((p - y))
    
        w = w - lr * dL_dw
        b = b - lr * dL_db

    return (w, b)