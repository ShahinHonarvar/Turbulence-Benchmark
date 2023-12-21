import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] < 2 or matrix.shape[1] < 2:
        return []
    return [list(row) for row in np.where(np.sum(matrix, axis=1) == -452)[0]]
