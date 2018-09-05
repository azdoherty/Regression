import numpy as np


def objective_function(X, m, b):
    print("merge")
    res = np.sum((X[:, 1] - (m*X[:,0] - b))**2)
    print("test")
    return res

