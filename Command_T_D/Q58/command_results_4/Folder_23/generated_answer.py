import numpy as np
def submatrix_with_n_numbers(arr):
    if arr.size == 0:
        return 0
    return np.sum(np.all(np.where(np.sum(np.bincount(arr), min_num=69), arr)))
