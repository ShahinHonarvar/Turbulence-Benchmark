import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.where(np.sum(matrix, axis=2) == -4, matrix, np.empty(matrix.shape)).tolist()
