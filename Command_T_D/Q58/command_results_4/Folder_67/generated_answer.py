import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.sum(np.sum(arr, axis=2), axis=1) == 43)
