import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.any(np.all(arr[i:j+1] == np.full(len(arr[i:j+1]), 120), axis=1), axis=0))
