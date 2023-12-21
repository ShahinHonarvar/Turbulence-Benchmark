import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.all(matrix == 118, axis=1), axis=0))
