import numpy as np
def submatrix_with_n_numbers(arr):
    m = len(arr)
    n = len(arr[0])
    if m < n:
        return 0
    if m == 1:
        return arr[0].count(56)
    return arr.count(56, axis=1).sum()
