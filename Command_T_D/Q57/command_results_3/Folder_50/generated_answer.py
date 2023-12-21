import numpy as np
def submatrix_with_particular_sum(arr):
    res = []
    for i in range(len(arr)):
        if np.sum(arr[:i]) + np.sum(arr[i+1:]) == 95:
            res.append(arr[:i] + arr[i+1:])
    return res
