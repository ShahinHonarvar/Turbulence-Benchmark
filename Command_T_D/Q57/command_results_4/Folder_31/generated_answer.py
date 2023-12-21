import numpy as np
def submatrix_with_particular_sum(arr):
    return np.where(np.sum(arr, axis=2) == -44, arr, np.empty(0, dtype=np.int64)).tolist()
