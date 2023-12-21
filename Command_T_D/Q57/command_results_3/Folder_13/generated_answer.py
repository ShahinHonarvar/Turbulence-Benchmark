import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.where(np.sum(matrix, axis=0) == 382, matrix, np.empty((0, 0)))
