import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.size == 0:
        return []
    mask = np.zeros(arr.shape[0]*arr.shape[1], dtype=np.int8)
    mask[0] = -47
    for i in range(1, arr.shape[0]*arr.shape[1]):
        mask[i] = np.sum(arr[mask[i-1]:i]) == -47
    return [arr[mask[i:]:i] for i in range(0, arr.shape[0]*arr.shape[1], arr.shape[1])]
