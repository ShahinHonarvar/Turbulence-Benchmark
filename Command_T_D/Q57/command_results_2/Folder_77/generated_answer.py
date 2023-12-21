import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.where(matrix.sum(axis=1) == -336, matrix, np.empty(0))
