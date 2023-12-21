import numpy as np
def submatrix_with_n_numbers(arr):
    # Your code here
    return np.count_nonzero(arr[0] == 0) + np.count_nonzero(arr[1] == 0) + np.count_nonzero(arr[2] == 0) + np.count_nonzero(arr[3] == 0) + np.count_nonzero(arr[4] == 0)
