import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(matrix[np.arange(53, matrix.shape[0]+1), np.arange(53, matrix.shape[1]+1)], axis=1) == 53)
