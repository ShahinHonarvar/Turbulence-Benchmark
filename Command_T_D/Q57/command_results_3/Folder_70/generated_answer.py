import numpy as np
def submatrix_with_particular_sum(matrix):
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = (matrix[i][j], i, j)
    matrix.sort()
    for i in range(len(matrix)):
        s = 0
        for j in range(i, len(matrix)):
            s += matrix[i][j][0]
            matrix[i][j] = (s, i, j)
    for i in range(len(matrix)):
        s = 0
        for j in range(i, len(matrix)):
            s += matrix[i][j][0]
            res.append((i, j, s))
    return res
