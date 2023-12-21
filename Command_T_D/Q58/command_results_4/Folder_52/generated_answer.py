import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.logical_and(matrix[0][:147] == 147, np.all(matrix[1:] == 147, axis=1)))
