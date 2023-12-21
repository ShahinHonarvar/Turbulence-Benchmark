import numpy as np
def submatrix_with_particular_sum(arr):
    res = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            suma = 0
            for k in range(j, len(arr[0])):
                suma += arr[i][k]
            if suma == -93:
                res.append(arr[i][:j] + arr[i][j:k] + arr[i][k+1:])
    return res
