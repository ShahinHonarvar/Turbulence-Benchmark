import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.shape[0] < 3:
        return []
    # Get all submatrices with the correct sum
    return [submatrix for i in range(1, arr.shape[0] - 1) for j in range(1, arr.shape[1] - 1) for submatrix in arr[i - 1:i + 2, j - 1:j + 2]]
