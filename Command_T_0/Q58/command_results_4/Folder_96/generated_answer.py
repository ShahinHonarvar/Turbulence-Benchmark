import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:i+20] == matrix[i:i+20], axis=1) for i in range(len(matrix) - 19))
