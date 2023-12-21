import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:i+107] == matrix[i:i+107], axis=1) for i in range(len(matrix) - 106))
