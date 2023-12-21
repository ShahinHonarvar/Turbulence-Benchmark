import numpy as np
def submatrix_with_particular_sum(arr):
    res = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            cur_sum = 0
            for k in range(j, len(arr[i])+1):
                cur_sum += arr[i][k]
            if cur_sum == -46:
                res += [[arr[i][j], arr[i][k+1]]
    return res
