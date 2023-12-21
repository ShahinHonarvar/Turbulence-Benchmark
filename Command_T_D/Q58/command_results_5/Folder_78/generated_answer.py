import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.bincount(matrix) == 91, axis=0), axis=0)
