import numpy as np
def submatrix_with_particular_sum(matrix):
    rows = np.full((matrix.shape[0] + 1), -936)
    for row in range(matrix.shape[0]):
        rows[row] = np.sum(matrix[row])
    return np.where(rows == -936)
