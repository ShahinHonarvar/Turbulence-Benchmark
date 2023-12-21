import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(np.sum(np.sum(matrix == 147, axis=1), axis=2), axis=3) == 147)
