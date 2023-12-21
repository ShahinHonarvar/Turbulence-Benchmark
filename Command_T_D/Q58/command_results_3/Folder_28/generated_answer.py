import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(np.sum(matrix, axis=0) == 37, 1, 0) == 3)
