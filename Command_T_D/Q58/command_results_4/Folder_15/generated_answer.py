import numpy as np
def submatrix_with_n_numbers(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                res += 1
            else:
                break
    return res
