import numpy as np
def submatrix_with_particular_sum(arr):
    res = []
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            temp = arr[i][j]
            if temp == 69:
                res += [[arr[i][j]]
            elif temp < 69:
                res += [[arr[i][j]] + [arr[i][j+1]]
            elif temp > 69:
                res += [[arr[i][j]] + [arr[i+1][j]]
    return res
