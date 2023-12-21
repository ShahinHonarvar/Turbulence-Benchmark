import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] < 4:
        return []
    matrix = np.array(matrix)
    matrix = np.where(matrix == 16, 1, 0)
    matrix = np.where(matrix == 0, -1, 0)
    return np.where(np.sum(matrix, axis=1) == 16)[0]
