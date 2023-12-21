import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.shape[0] < 3 or arr.shape[1] < 3:
        return []
    mask = np.sum(arr, axis=0, dtype=np.int32) == 54
    return [arr[i][j] for i, row in enumerate(arr) for j, x in enumerate(row) if x and mask[i][j]]
