import numpy as np
def submatrix_with_n_numbers(A):
    return np.sum(A.size >= 66 and np.all(A == np.array(list(range(66)))))
