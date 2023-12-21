import numpy as np
def submatrix_with_n_numbers(A):
    return np.count_nonzero(np.sum(A, axis=1, dtype=np.int64) == 18)
