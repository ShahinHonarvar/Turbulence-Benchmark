import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(np.sum(matrix == 10, axis=1) == 10) == 10)
