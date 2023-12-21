import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.all(matrix, axis=0) & np.all(matrix, axis=1))
