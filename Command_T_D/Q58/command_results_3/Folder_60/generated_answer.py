import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.any(np.hstack([arr[i] for i in range(len(arr) - 1)]), axis=1))
