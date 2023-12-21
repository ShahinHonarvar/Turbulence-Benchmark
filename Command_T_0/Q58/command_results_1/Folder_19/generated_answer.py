import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix == 17, axis=1))
