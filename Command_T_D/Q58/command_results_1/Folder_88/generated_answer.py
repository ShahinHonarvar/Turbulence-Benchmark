import numpy as np
def submatrix_with_n_numbers(arr):
    if arr.shape[0] < 67:
        return 0
    return np.sum(np.where(np.all(arr[x:x + 67] == x, axis=1), 1, 0) for x in range(arr.shape[0] - 66))
