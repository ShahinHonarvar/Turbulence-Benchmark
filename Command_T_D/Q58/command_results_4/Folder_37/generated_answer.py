import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(arr.shape[0] >= 64 and arr.shape[1] >= 64)
