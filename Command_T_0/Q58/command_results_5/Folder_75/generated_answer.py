import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:i+80] == matrix[i:i+80], axis=1) for i in range(0, len(matrix), 80))
