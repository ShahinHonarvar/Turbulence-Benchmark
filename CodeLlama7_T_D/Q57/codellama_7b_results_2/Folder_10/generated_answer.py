
import numpy as np
def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            sum = 0
            for row in range(i, i + 2):
                for col in range(j, j + 2):
                    sum += matrix[row][col]
            if sum == 56:
                submatrices.append([matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j]], [matrix[i + 1][j + 1]]))
    return submatrices
