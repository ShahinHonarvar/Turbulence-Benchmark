import numpy as np
def submatrix_with_particular_sum(arr):
    return [row for row in np.where(np.sum(arr, axis=1) == 41)[0]]
