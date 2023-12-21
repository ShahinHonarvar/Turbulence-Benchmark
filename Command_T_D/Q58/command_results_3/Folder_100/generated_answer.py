import numpy as np
def submatrix_with_n_numbers(A):
    return np.count_nonzero(np.any(A.reshape(-1, 10), axis=1))
