import numpy as np
def submatrix_with_n_numbers(matrix):
    if matrix.shape[0] < matrix.shape[1]:
        matrix = np.rot90(matrix)
    return np.sum(np.count_nonzero(matrix, axis=0) == 76)
