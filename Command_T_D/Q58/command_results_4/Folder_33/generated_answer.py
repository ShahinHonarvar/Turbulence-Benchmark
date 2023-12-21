import numpy as np
def submatrix_with_n_numbers(mat):
    return np.count_nonzero(mat[::2] == 118)
