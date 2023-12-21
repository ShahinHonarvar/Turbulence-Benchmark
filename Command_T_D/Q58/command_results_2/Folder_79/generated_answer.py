import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.logical_and(matrix[0] == 60, matrix[1] == 60))
