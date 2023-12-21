import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.sum(matrix, axis=1) == 60, axis=1))
