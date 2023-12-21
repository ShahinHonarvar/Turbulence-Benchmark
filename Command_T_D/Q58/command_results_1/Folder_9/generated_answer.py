import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.all(matrix == np.full(33, -1), axis=2))
