import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.where(np.sum(matrix, axis=1) == 16, matrix, np.empty(matrix.shape))
