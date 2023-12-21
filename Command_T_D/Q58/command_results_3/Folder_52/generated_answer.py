import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(matrix[::147], axis=0) == 147)
