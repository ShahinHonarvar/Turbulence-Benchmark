import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[x:x+n] == 138 for x in range(0, matrix.shape[0] - n)))
