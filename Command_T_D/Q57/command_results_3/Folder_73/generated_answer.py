import numpy as np
def submatrix_with_particular_sum(arr):
    if not arr:
        return []
    if arr.shape[0] == 1:
        return [[arr]]
    return [[arr[i:j + 1] for i in range(0, arr.shape[0] - 1)]
