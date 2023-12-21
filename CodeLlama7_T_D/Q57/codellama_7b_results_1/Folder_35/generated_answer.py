
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            submatrix = matrix[i][j]
            if sum(submatrix) == 432:
                submatrices.append(submatrix)
    return submatrices
