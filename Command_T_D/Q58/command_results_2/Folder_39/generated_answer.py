import numpy as np
def submatrix_with_n_numbers(arr):
    if arr.shape[0] < 3:
        return 0
    return np.sum(np.any(np.all(arr[i:j+2] == 59, axis=1) for i in range(0, arr.shape[0]-2) for j in range(i+1, arr.shape[0]-1)))
