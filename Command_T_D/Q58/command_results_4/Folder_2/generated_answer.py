import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[row:row+107] == matrix[row:row+107], axis=1))
