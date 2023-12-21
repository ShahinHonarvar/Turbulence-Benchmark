import numpy as np
def submatrix_with_particular_sum(arr):
    rows = np.where(np.sum(arr, axis=1) == 40)[0]
    return [[arr[r][:i] for r in rows] for i in range(len(arr[0]))]
