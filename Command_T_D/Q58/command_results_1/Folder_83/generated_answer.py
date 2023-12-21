import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(np.sum(arr == 47, axis=1) == 47)
