import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(np.any(np.any(mat == i, axis=2), axis=1)) == 87
