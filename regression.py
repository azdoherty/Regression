import numpy as np


def objective_function(X, m, b):
    res = np.sum((X[:, 1] - (m*X[:,0] - b))**2)
    print(np.sqrt(res))
    return res

