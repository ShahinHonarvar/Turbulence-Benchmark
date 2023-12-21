import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(arr == 111, axis=1))
