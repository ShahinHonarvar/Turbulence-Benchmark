import numpy as np
def submatrix_with_particular_sum(arr):
    # Find all submatrices of size (4, 3) that sum to 432
    return np.where(np.sum(arr[i:i + 4, j:j + 3], axis=1) == 432 for i in range(0, len(arr) - 3) for j in range(0, len(arr[0]) - 2))
