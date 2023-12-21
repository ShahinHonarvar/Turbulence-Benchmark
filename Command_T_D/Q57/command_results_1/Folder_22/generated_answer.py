import numpy as np
def submatrix_with_particular_sum(arr):
    return np.where(np.all(np.equal(np.sum(arr, axis=0), -38)), arr)
