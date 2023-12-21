import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.logical_and(matrix[0] == 64, np.all(matrix[1:] == 64, axis=1)))
