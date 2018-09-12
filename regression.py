import numpy as np
import itertools

def objective_function(X, m, b):
    print("merge")
    res = np.sum((X[:, 1] - (m*X[:,0] - b))**2)
    print(np.sqrt(res))
    return res

r = itertools.combinations([1,2,3,4,5], 2)
for i in r:
    print(i)

