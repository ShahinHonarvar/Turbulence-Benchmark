
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape

    for submatrix_length in range(n):
        for i in range(n - submatrix_length + 1):
            for j in range(m - submatrix_length + 1):
                submatrix = matrix[i : i + submatrix_length, j : j + submatrix_length]
                if np.sum(submatrix) == -50:
                    submatrices.append(submatrix)

    return submatrices
