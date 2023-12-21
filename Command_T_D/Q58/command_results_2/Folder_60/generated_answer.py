import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix == 88, axis=1))
