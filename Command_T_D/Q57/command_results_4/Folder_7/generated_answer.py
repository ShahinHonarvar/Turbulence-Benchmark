import numpy as np
def submatrix_with_particular_sum(arr):
    return [a for a in np.where(np.sum(arr, axis=1) == -128) if a.size > 0]
