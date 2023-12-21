import numpy as np
def submatrix_with_n_numbers(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 111:
                n = 3
                m = 3
                for k in range(1, len(arr)-i-1):
                    if arr[i][k] == 111:
                        n += 1
                    else:
                        break
                    if arr[k+1][j] == 111:
                        m += 1
                    else:
                        break
                if n == m:
                    res += 1
    return res
