import numpy as np
def submatrix_with_particular_sum(arr):
    return [np.array(r) for r in np.where(arr == 2)]
