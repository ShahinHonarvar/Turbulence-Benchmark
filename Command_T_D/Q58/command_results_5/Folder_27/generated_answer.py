import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(matrix == 77, axis=1) == 77)
