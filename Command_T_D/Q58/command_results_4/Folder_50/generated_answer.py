import numpy as np
def submatrix_with_n_numbers(mat):
    return np.count_nonzero(np.any(mat == 40, axis=1))
