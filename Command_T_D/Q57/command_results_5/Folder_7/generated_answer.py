import numpy as np
def submatrix_with_particular_sum(arr):
    return np.where(np.all(arr == -128, axis=1))[0]
