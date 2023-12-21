import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(np.any(arr == 111, axis=1), axis=0)
