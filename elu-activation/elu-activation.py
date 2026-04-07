def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    if alpha < 0 :
        raise ValueError("Alpha should be greater or equal to 0 .")

    elu = []
    for x_i in x:
        if x_i > 0:
            elu.append(x_i)
        else:
            exp = math.exp(x_i)
            elu.append(alpha * (exp - 1)) 

    return elu
    