import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    x = np.array(x, dtype=float)

    selu_list = []

    for x_i in x :
        if x_i > 0:
            val = lam * x_i
        else:
            val = lam * alpha * (np.exp(x_i) - 1)
            
        selu_list.append(round(float(val), 4))

    return selu_list
