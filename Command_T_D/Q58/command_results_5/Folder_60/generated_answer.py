import numpy as np
def submatrix_with_n_numbers(arr):
    n = len(arr)
    m = len(arr[0])
    res = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(i, n):
                cnt += arr[k][j] > arr[i][j]
            if cnt == 88:
                res += 1
    return res
