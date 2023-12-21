import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(np.any(matrix == 66, axis=1), matrix == 66, matrix == 0))
