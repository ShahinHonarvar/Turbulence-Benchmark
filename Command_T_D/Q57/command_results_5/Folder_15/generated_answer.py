import numpy as np
def submatrix_with_particular_sum(arr):
    m = len(arr)
    n = len(arr[0])
    if m == 1:
        return []
    res = []
    for i in range(m):
        for j in range(n):
            s = arr[i][j]
            if s == -9:
                res.append((arr[:i] + arr[i+1:m] + arr[i:j+1] + arr[j+1:n]))
                break
    return res
