import numpy as np
def submatrix_with_n_numbers(matrix):
    if not matrix.flags['C_CONTIGUOUS']:
        matrix = np.ascontiguousarray(matrix)
    return np.sum(np.count_nonzero(matrix, axis=1) == 41)
