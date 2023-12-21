import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(np.isin(arr, 42), axis=0))
