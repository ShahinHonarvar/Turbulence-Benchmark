import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.count_nonzero(matrix, axis=0) == 63 and np.count_nonzero(matrix, axis=1) == 63)
