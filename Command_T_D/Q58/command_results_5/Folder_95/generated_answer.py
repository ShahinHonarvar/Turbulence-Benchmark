import numpy as np
def submatrix_with_n_numbers(arr):
    if arr.size == 0:
        return 0
    height = len(arr)
    width = len(arr[0])
    return np.sum(np.sum(arr, axis=1) == 87) // 87 * np.sum(np.sum(arr, axis=0) == 87) // 87
