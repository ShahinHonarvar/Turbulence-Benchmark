import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.shape[0] == 1:
        return []
    target = np.full(arr.shape[0], 862)
    return np.where(np.sum(arr, axis=1) == target)[0].tolist()
