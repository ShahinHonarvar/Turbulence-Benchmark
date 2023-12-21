import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(arr.reshape(-1, arr.shape[1]).T.reshape(-1, 10).T == 10)
