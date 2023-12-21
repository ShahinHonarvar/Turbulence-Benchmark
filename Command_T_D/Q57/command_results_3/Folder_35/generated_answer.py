import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    if sum(matrix.sum(axis=1)) != 432:
        return []
    return [[sum(matrix[row][:]) == 432 for row in range(matrix.shape[0])]]
