import numpy as np
def submatrix_with_particular_sum(arr):
    return [s for s in np.where(np.sum(arr, axis=1) == -185)]
