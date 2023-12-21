import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.shape[0] < arr.shape[1]:
        return []
    res = []
    for i in range(arr.shape[0] - 1):
        for j in range(arr.shape[1] - 1):
            curr = arr[i][j] + arr[i + 1][j] + arr[i][j + 1] + arr[i + 1][j + 1]
            if curr == 95:
                res.append(arr[i:i + 2][j:j + 2])
    return res
