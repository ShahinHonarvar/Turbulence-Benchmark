import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(np.sum(arr, axis=1) == 69)
