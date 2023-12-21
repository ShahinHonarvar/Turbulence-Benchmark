import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(matrix == np.array([34] * 34), matrix, np.nan), axis=1) == 34)
