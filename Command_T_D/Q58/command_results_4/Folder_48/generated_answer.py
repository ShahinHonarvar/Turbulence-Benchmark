import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[0:130] == matrix[1:], axis=1))
