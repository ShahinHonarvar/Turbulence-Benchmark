import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.any(matrix == 17, axis=1))
