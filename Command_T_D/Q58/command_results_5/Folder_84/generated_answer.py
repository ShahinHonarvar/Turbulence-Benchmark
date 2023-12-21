import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(arr.astype(np.int8).toarray() == 127)
