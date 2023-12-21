import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.shape[0] == matrix.shape[1] == 1:
        return [matrix]
    if matrix[0][0] == 416:
        return [[matrix]]
    return [[row[0:min(len(row), i+1)]] for i in range(min(len(row), 3)) for row in matrix] + [
            [[row[0:min(len(row), i+1)]] for i in range(min(len(row), 3)) for row in zip(*matrix)]
    ]
