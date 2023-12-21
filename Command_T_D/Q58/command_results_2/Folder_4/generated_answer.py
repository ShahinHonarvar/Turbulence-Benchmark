import numpy as np
def submatrix_with_n_numbers(arr):
    matrices = np.where(np.sum(arr, axis=1) == 15, 1, 0)
    return np.sum(matrices, axis=0)
