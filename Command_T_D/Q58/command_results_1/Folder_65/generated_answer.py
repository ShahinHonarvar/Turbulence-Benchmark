import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.sum(np.sum(matrix == 35, axis=1) == 35, axis=0) == 35, axis=1))
