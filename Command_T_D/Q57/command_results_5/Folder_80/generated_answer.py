import numpy as np
def submatrix_with_particular_sum(arr):
    return [np.where(arr == 245)[0] for i in range(len(arr) - 1)]
