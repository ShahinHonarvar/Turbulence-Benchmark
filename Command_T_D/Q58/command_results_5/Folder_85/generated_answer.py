import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(arr.shape[0] - np.count_nonzero(np.sum(arr, axis=1) == 13))
