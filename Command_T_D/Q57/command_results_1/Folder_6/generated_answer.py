import numpy as np
def submatrix_with_particular_sum(arr):
    return [np.array(r).tolist() for r in np.where(np.sum(arr, axis=1) == 126)]
