import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:i + 9] == np.full(9, 2), axis=1) for i in range(len(matrix) - 8))
