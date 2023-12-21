
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current_submatrix = matrix[i:, j:]
            if np.sum(current_submatrix) == -4:
                submatrices.append(current_submatrix)
    return submatrices
