import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.all(np.isin(matrix, 94), axis=2))
