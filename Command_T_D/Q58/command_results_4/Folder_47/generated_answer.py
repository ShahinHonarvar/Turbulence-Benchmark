import numpy as np
def submatrix_with_n_numbers(arr):
    return np.count_nonzero(np.all(np.vstack(arr), axis=0), axis=1)
