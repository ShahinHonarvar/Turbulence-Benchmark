import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] * matrix.shape[1] == 0:
        return []
    matrix = np.array(matrix)
    return [[row[row.nonzero()].tolist() for row in matrix]]
