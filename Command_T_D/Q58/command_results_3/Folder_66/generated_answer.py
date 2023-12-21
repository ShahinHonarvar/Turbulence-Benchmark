import numpy as np
def submatrix_with_n_numbers(arr):
    m, n = arr.shape
    if m > n:
        return 0
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i][j] == 42:
                count += 1
                if count == m:
                    break
    return count
