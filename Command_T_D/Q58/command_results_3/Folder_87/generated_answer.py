import numpy as np
def submatrix_with_n_numbers(arr):
    return np.where(np.sum(np.abs(np.sum(arr, axis=1)), axis=1) == 96, 1, 0).sum()
