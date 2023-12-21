import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    if len(matrix) < 126:
        return 0
    mask = np.sum(np.sum(matrix == -1, axis=1), axis=1) == 126
    return np.sum(mask)
