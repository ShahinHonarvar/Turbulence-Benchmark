import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.shape[0] == 1:
        return []
    return np.where(np.sum(arr, axis=1) == -83)[0]
