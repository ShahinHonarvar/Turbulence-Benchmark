import numpy as np
def submatrix_with_particular_sum(arr):
    if np.sum(arr, axis=1) == 416:
        return [arr[i][:j] for i in range(len(arr)) for j in range(i+1, len(arr[i]))]
    else:
        return []
