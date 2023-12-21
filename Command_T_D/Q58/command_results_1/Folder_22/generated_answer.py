import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(matrix.shape[0] * matrix.shape[1] == 21)
