import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here

    D = len(x_t)
    H = len(h_prev)
    if D < 1 or H > 256:
        return

    input_cont = np.dot(x_t, Wx)
    recurrent_cont = np.dot(h_prev, Wh)

    return np.tanh(input_cont + recurrent_cont + b)
