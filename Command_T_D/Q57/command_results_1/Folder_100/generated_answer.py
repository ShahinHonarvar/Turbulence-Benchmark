import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    return np.where(np.sum(matrix, axis=1) == 28, matrix, np.empty(matrix.shape))
