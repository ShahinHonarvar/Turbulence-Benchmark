import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(np.sum(matrix, axis=0) == 72, axis=1) == 72)
