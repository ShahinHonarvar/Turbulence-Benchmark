import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:i+33] == matrix[i:i+33], axis=1) for i in range(len(matrix) - 32))
