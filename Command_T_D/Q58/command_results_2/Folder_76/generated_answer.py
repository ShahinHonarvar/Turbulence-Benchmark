import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(np.where(np.sum(arr == 159, axis=1) == 3))
