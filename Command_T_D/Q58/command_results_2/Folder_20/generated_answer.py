import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.where(np.any(arr == 49, axis=1), True, False))
