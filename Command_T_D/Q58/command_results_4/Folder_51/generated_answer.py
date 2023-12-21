import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.count_nonzero(matrix, axis=1) == 95)
