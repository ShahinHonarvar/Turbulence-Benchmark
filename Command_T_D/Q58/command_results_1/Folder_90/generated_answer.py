import numpy as np
def submatrix_with_n_numbers(A):
    n = 176
    return np.count_nonzero(np.sum(A, axis=1, dtype=np.int32) == n)
