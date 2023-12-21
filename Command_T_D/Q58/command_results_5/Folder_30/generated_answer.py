import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(np.all(arr[i] == 94 for i in range(len(arr) - 1)))
