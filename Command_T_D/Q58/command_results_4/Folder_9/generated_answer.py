import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(np.all(np.where(arr[i] == 33, arr[i+1:i+34], -1) == [0, 1, 2, 3] for i in range(len(arr) - 32)))
