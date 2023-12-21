import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.any(matrix == 83, axis=1), axis=0))
