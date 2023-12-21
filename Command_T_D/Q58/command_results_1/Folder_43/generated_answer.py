import numpy as np
def submatrix_with_n_numbers(arr):
    m, n = arr.shape
    return sum(np.sum(arr[r:r + 85], axis=1) == 85 for r in range(0, m, 85))
