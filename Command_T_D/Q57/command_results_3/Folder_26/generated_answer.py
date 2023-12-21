import numpy as np
def submatrix_with_particular_sum(arr):
    m = np.sum(arr, axis=0) == 997
    return [arr[i][:j] for i, row in enumerate(arr) for j, col in enumerate(row) if m[i][j]]
