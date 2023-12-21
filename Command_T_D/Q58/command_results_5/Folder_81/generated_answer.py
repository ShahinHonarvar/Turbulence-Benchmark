import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.where(np.sum(matrix, axis=0) == 97, True, False), axis=1)
