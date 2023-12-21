import numpy as np
def submatrix_with_n_numbers(matrix):
    if len(matrix) == 0:
        return 0
    if len(matrix[0]) == 0:
        return 0
    if len(matrix) == 1:
        return 1
    return np.sum(np.count_nonzero(np.all(matrix[0] == 49, axis=1)))
