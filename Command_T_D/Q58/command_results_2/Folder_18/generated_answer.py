import numpy as np
def submatrix_with_n_numbers(arr):
    if not arr.flags['OWNDATA']:
        arr = np.array(arr)
    return np.sum(np.sum(np.sum(arr, axis=1), axis=2), axis=3) == 104)
