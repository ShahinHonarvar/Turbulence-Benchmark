import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.sum(matrix, axis=1) == 93, axis=1))
