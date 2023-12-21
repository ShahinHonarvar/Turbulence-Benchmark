import numpy as np
def submatrix_with_particular_sum(matrix):
    if not matrix:
        return []
    if matrix.shape[0] == 1:
        return [matrix]
    if matrix.shape[1] == 1:
        return [[matrix[0]]]
    result = []
    for i in range(0, matrix.shape[0] - 1):
        for j in range(0, matrix.shape[1] - 1):
            if matrix[i][j] == 66:
                result += [[matrix[i][:j] + matrix[i + 1][j + 1:]]
    return result
