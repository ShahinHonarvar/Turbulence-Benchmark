import numpy as np
def submatrix_with_particular_sum(arr):
    m, n = arr.shape
    submats = []
    for i in range(m):
        for j in range(n):
            suma = 0
            for k in range(i, m):
                suma += arr[i][k]
            for k in range(j, n):
                suma += arr[k][j]
            if suma == 92:
                submats.append(arr[i][:][:])
    return submats
