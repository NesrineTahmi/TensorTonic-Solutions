import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    Q_new = np.array(Q, dtype=float).copy()
    
    best_next = float(np.max(Q_new[s_next]))
    
    target = float(r) + gamma * best_next
    error = target - float(Q_new[s, a])
    
    Q_new[s, a] += alpha * error
    
    return Q_new