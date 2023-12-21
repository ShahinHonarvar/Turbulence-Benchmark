import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.sum(matrix == 87, axis=2), axis=1))
