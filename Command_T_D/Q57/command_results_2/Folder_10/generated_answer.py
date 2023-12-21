import numpy as np
def submatrix_with_particular_sum(arr):
    return np.where(np.all(np.sum(arr, axis=0) == 56, axis=1))[0]
