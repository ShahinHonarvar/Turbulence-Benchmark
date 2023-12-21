import numpy as np
def submatrix_with_n_numbers(A):
    return np.count_nonzero(np.any(A == 15, axis=1), axis=0)
