import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(np.where(np.where(mat == 57, True, False)[0], True, False)[1] == 57)
