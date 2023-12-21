
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            current_submatrix = matrix[i:, j:]
            if np.sum(current_submatrix) == -83:
                submatrices.append(current_submatrix)
    return submatrices
