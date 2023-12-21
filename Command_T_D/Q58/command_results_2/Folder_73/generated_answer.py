import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.all(matrix == 41, axis=2))
