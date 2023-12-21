import numpy as np
def submatrix_with_particular_sum(arr):
    m = len(arr)
    n = len(arr[0])
    if m == 0 or n == 0:
        return []
    mat = np.matrix(arr, dtype=np.int32)
    return np.where(np.sum(mat, axis=1) == -36, mat.tolist(), []).tolist()
