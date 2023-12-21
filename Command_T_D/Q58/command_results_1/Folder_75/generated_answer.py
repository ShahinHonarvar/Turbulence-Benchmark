import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(np.where(np.sum(mat, axis=1) == 80, 1, 0) == 80)
