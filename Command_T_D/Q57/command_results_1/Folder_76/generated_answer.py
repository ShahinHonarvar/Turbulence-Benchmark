import numpy as np
def submatrix_with_particular_sum(arr):
    res = []
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            val = arr[i][j]
            if val == -255:
                res += [arr[i][:j]+arr[i+1:][:j]+arr[i][j+1:]+arr[i+1:][j+1:]]
    return res
