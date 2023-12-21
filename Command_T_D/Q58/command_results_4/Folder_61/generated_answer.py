import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(arr[::2] == arr[::2][1:3] == arr[1::2] == arr[1::2][1:3] == 4)
