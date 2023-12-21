import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.matrix(matrix)
    return matrix.sum() // matrix.shape[0] // matrix.shape[1]
