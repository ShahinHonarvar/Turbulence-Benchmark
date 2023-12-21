import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(np.sum(matrix, axis=1) == 180, 1, 0) == 0)
