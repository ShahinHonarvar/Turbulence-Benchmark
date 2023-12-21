import numpy as np
def submatrix_with_particular_sum(arr):
    mask = np.sum(arr == 66, axis=0) == 4
    return [arr[mask]]
