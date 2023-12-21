import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.where(np.sum(arr == 47, axis=2), True, False)[0])
