import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix == 131, axis=2), axis=1)
