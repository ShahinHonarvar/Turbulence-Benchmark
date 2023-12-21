import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(np.all(arr[i:j] == np.arange(1, 121) for i in range(0, len(arr) - 120) for j in range(i, len(arr) - 1)))
