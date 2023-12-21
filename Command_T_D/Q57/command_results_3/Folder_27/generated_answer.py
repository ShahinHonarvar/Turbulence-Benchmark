import numpy as np
def submatrix_with_particular_sum(arr):
    res = []
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr[0])-1):
            curr_sum = arr[i][j]
            curr_sum += arr[i][j+1]
            curr_sum += arr[i+1][j]
            curr_sum += arr[i+1][j+1]
            if curr_sum == 77:
                res += [[arr[i][:j+2], arr[i+1][j+2:]]
    return res
