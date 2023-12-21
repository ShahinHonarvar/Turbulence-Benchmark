import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(matrix.shape[0] * matrix.shape[1] * (matrix.shape[0] - 1) * (matrix.shape[1] - 1))
