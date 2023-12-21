import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.sum(matrix, axis=1) == 68, axis=1))
