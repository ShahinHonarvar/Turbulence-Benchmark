import numpy as np
def submatrix_with_particular_sum(arr):
    return np.where(np.sum(arr,axis=1) == -308)[0]
