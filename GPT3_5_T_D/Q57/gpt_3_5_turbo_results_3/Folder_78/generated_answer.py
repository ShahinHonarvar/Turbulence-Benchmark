
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for m in range(i + 1, matrix.shape[0] + 1):
                for n in range(j + 1, matrix.shape[1] + 1):
                    submatrix = matrix[i:m, j:n]
                    if np.sum(submatrix) == 17:
                        submatrices.append(submatrix.tolist())
    return submatrices
