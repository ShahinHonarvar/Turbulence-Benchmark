import numpy as np
def submatrix_with_n_numbers(mat):
    return np.count_nonzero(np.sum(mat == 0, axis=1) == 76)
