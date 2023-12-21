import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.logical_and(matrix[0][:80] == 1, matrix[1][:80] == 1))
