import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.asarray(np.where(np.sum(arr, axis=1) == 104, arr, np.nan)))
