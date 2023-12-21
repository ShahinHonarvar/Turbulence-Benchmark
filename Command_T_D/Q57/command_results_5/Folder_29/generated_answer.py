import numpy as np
def submatrix_with_particular_sum(arr):
    return [sub for sub in np.split(arr, 84, axis=1) if np.sum(sub, axis=1) == 84]
