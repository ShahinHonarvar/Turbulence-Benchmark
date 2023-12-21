import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(matrix.shape[0] * matrix.shape[1] == 4)
