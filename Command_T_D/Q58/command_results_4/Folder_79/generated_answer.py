import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return np.sum(np.any(matrix[1:][:59] == matrix[1:][60:], axis=1))
