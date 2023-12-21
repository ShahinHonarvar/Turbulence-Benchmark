import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.shape[0] == 1:
        return []
    else:
        return [arr[i:i + 2] for i in range(0, arr.shape[0] - 1)]
