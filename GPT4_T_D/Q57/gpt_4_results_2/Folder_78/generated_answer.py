
import numpy as np

def submatrix_with_particular_sum(matrix):

    submatrices = []

    row_len = matrix.shape[0]
    column_len = matrix.shape[1]

    for size in range(1, min(row_len, column_len) + 1):
        for i in range(row_len - size + 1):
            for j in range(column_len - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.sum(submatrix) == 17:
                    submatrices.append(submatrix.tolist())

    return submatrices
