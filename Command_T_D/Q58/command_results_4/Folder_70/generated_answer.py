import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return np.sum(np.sum(np.sum(matrix == 173, axis=2), axis=1) == 173)
