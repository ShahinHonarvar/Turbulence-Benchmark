import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.all(np.sum(matrix, axis=1) == 92, axis=1))
