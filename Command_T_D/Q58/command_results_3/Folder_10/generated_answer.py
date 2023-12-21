import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(matrix == 0, axis=1) == 56)
