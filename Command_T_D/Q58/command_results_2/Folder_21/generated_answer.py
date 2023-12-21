import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(np.all(arr == 139, axis=1))
