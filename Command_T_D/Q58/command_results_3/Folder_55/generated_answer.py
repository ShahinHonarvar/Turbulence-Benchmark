import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[start:end, start:end] == 39, axis=1))
