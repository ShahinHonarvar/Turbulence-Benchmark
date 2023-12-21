
import numpy as np

def submatrix_with_particular_sum(matrix):
    def matrix_sum(matrix, i1, j1, i2, j2):
        return np.sum(matrix[i1:i2+1, j1:j2+1])

    submatrices = []
    rows, columns = matrix.shape

    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    if matrix_sum(matrix, i, j, k, l) == 88:
                        submatrices.append(matrix[i:k+1, j:l+1])

    return submatrices
