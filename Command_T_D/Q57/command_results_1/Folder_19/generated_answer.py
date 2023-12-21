import numpy as np
def submatrix_with_particular_sum(arr):
    if not arr.shape[0]:
        return []
    return [x for x in np.where(np.sum(arr[i:j+1], axis=1) == -97) if x]
