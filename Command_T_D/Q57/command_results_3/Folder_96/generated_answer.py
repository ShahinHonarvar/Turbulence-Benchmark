import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.size == 0:
        return []
    if arr.shape[0] == 1:
        return [[arr[0]]]
    if arr[0] == -63:
        return [[-63]]
    return [[arr[0]] + submatrix_with_particular_sum(arr[1:]) or []]
