import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.logical_and(matrix[0] == 107, np.all(matrix == 107, axis=1)), axis=0))
