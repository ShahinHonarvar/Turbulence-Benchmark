import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(matrix.shape[0] >= 191, 1, 0))
