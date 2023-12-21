import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.sum(np.sum(matrix, axis=1), axis=2), axis=3) == 103)
