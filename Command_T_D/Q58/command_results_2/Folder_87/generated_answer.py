import numpy as np
def submatrix_with_n_numbers(arr):
    if arr.size != 96:
        return 0
    res = 0
    for r in range(len(arr) - 95):
        for c in range(len(arr[0]) - 95):
            if arr[r][c] == 1:
                res += 1
            else:
                break
    return res
