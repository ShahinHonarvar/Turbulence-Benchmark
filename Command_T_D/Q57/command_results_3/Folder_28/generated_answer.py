import numpy as np
def submatrix_with_particular_sum(arr):
    return np.where(arr.sum(axis=1) == 15, np.array(arr, dtype=np.int32), np.empty(0, dtype=np.int32))
