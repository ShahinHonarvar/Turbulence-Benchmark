import numpy as np
def submatrix_with_n_numbers(arr):
    res = np.sum(np.sum(arr, axis=1) == 69, axis=0)
    return res.item()
