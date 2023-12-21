import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return np.sum(np.where(np.sum(matrix, axis=1) == 48, 1, 0))
