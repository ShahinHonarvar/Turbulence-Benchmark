import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.any(np.sum(arr, axis=0) == 7, axis=1))
