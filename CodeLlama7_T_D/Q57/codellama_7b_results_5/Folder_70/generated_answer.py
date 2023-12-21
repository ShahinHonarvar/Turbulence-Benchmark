
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum = 0
            for k in range(i, len(matrix) - (len(matrix) - i))):
                sum += matrix[k][j]
            if sum == 411:
                submatrices.append((i, j, sum)))
    return submatrices
