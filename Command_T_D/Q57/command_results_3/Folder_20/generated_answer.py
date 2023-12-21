import numpy as np
def submatrix_with_particular_sum(arr):
    return [x for x in np.where(np.sum(arr, axis=1) == -57)[0] if len(x) > 0]
