import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(matrix.shape[0] >= 80 and matrix.shape[1] >= 80, 1, 0))
