import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.sum(matrix, axis=0) == np.sum(matrix, axis=1) == 73)
