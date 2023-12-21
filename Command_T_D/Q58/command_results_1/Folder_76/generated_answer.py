import numpy as np
def submatrix_with_n_numbers(arr):
    m, n = len(arr), len(arr[0])
    cnt = 0
    for i in range(m):
        for j in range(n):
            cnt += (i == 0) + (j == 0) + (i == m-1) + (j == n-1)
            cnt -= arr[i][j] < 159
            cnt += arr[i][j] == 159
    return cnt
