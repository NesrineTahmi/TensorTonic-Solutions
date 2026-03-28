def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x_t = x0
    
    for i in range(steps):
        f_prime = 2*a*x_t + b
        x_t_plus_1 = x_t - lr * f_prime
        x_t = x_t_plus_1

    return x_t