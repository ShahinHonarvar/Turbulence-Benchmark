import numpy as np
def submatrix_with_particular_sum(arr):
    res = []
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            if arr[i][j] + arr[i+1][j] + arr[i][j+1] + arr[i+1][j+1] == 28:
                res.append((arr[i][:j+1], arr[i+1][:j+1], arr[i][j+1:], arr[i+1][j+1:]))
    return res
