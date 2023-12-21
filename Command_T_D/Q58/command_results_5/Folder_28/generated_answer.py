import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(np.sum(matrix == 37, axis=1) == 37, matrix == 37, np.zeros_like(matrix)) == 37)
