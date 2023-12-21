
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix = matrix[i:i+1, j:j+1]
            if np.sum(submatrix) == 830:
                submatrices.append(submatrix)
    return submatrices
