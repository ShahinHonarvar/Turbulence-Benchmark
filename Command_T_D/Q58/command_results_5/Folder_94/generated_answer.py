import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(np.where(np.sum(arr, axis=1) == 93, axis=1), axis=0)))
