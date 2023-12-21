import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.count_nonzero(np.all(matrix == 83, axis=2))
