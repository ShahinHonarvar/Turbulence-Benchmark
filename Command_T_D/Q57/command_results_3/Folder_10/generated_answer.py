import numpy as np
def submatrix_with_particular_sum(matrix):
    res = []
    for i in range(len(matrix)):
        if matrix[i] == 56:
            res += [[i]]
            matrix[i] = 0
    if matrix[0] == 56:
        res += [[0]]
        matrix[0] = 0
    if matrix[len(matrix) - 1] == 56:
        res += [[len(matrix) - 1]]
        matrix[len(matrix) - 1] = 0
    if matrix[0] == 26 and matrix[len(matrix) - 1] == 26:
        res += [[0, len(matrix) - 1]]
        matrix[0] = 0
        matrix[len(matrix) - 1] = 0
    return res
