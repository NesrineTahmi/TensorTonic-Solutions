import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    # Write code here

    m_new = []
    v_new = []
    m_hat = []
    v_hat = []
    param_new = []
    for i in range(len(param)):
        
        m_new.append(beta1*m[i] + (1-beta1)*grad[i])
        v_new.append(beta2*v[i] + (1-beta2)*(grad[i])**2)
    
        m_hat.append(m_new[i] / (1 - beta1**t))
        v_hat.append(v_new[i] / (1 - beta2**t))
    
        param_new.append(param[i] - lr*(m_hat[i] / (np.sqrt(v_hat[i]) + eps )))


    return (param_new, m_new, v_new)