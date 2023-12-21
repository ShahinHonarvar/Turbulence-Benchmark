import numpy as np
def submatrix_with_particular_sum(arr):
    if np.sum(arr, axis=1) == 87:
        return [arr]
    return []
