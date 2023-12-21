import numpy as np
def submatrix_with_n_numbers(arr):
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(8):
                cnt += arr[i][j] == k
            if cnt == 8:
                return 1
    return 0
