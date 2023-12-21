import numpy as np
def submatrix_with_n_numbers(arr):
    if len(arr) < 38:
        return 0
    res = np.bincount(arr[1:-1, 1:-1], minlength=38)
    return res.count(38)
