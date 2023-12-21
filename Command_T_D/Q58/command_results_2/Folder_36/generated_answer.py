import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.any(matrix == i, axis=2), axis=1) for i in range(0, 131))
