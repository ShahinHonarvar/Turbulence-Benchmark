import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(matrix == 139, matrix == 139, 0) == 3)
