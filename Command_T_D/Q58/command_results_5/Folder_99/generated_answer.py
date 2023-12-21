import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(arr[i:i+146] == np.array([0] * 146), axis=1) for i in range(0, len(arr) - 145))
