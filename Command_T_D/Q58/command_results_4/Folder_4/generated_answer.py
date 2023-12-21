import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    matrix = matrix.reshape(-1, 15)
    return np.sum(np.all(matrix, axis=1))
