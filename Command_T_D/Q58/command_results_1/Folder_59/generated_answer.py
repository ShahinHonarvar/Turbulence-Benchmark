import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.sum(matrix == 1, axis=1) == 76)
