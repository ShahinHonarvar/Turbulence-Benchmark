import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.matrix(matrix)
    return matrix.size * (matrix.size - 1) // 2 - np.count_nonzero(np.all(matrix, axis=2))
