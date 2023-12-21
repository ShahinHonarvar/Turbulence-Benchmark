
import numpy as np
def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            current_submatrix = matrix[i][j]
            if sum(current_submatrix) == 17:
                submatrices.append(current_submatrix)
    return submatrices
