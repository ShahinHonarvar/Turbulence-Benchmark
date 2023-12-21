import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.where(matrix == 166, 1, 0)))
