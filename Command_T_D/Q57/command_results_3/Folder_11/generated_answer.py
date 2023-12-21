import numpy as np
def submatrix_with_particular_sum(arr):
    return [np.sum(arr[r:r + n + 1], axis=1) == 38 for r in range(len(arr) - n + 1) for n in range(1, min(r + 1, len(arr) - 1) + 1)]
