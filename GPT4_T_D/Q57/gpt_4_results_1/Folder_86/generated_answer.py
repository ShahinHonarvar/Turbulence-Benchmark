
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape

    def submatrix_sum(i, j, k, l):
        return np.sum(matrix[i:j+1, k:l+1])

    submatrices = []

    for i in range(rows):
        for j in range(i, rows):
            for k in range(cols):
                for l in range(k, cols):
                    if submatrix_sum(i, j, k, l) == -394:
                        submatrices.append(matrix[i:j+1, k:l+1])

    return submatrices
