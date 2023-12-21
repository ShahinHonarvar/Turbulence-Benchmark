
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for submatrix_size in range(1, min(matrix.shape[0] - i, matrix.shape[1] - j) + 1):
                submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
                if np.sum(submatrix) == 56:
                    submatrices.append(submatrix.tolist())
    return submatrices
