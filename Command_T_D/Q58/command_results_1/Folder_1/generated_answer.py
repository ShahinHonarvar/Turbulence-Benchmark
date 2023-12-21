import numpy as np
def submatrix_with_n_numbers(arr):
    if len(arr) < 2:
        return 0
    if len(arr[0]) < 2:
        return 0
    if len(arr) < 2 * 23:
        return 0
    if len(arr[0]) < 2 * 23:
        return 0
    return np.sum(np.any(arr[i:i + 23] == np.full(23, -1), axis=1) for i in range(len(arr) - 23))
