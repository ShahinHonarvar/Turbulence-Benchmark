import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(np.sum(arr, axis=1) == 24, axis=1))
