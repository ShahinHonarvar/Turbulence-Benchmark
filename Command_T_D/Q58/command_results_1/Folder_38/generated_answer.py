import numpy as np
def submatrix_with_n_numbers(arr):
    if arr.size == 0:
        return 0
    res = 0
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            cnt = 0
            for k in range(0, arr.shape[2]):
                cnt += arr[i][j][k]
            if cnt == 34:
                res += 1
    return res
