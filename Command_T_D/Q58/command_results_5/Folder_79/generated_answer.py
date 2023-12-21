import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.any(np.any(arr, axis=1), axis=2), axis=0)
