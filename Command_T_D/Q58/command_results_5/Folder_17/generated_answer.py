import numpy as np
def submatrix_with_n_numbers(A):
    return np.sum(np.sum(A == 166, axis=1) == A.shape[1])
