import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    if matrix.shape[0] == 0 or matrix.shape[1] == 0:
        return []
    return [[x[i][j] for i in range(matrix.shape[0])] for j in range(matrix.shape[1])]
