import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(matrix.sum(axis=1) == 173)[0] != -1)
