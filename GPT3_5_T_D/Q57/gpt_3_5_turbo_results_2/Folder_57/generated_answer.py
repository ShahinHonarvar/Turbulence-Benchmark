
import numpy as np

def submatrix_with_particular_sum(matrix):
    def all_submatrices(matrix):
        m, n = matrix.shape
        for i in range(m):
            for j in range(n):
                for k in range(i + 1, m + 1):
                    for l in range(j + 1, n + 1):
                        yield matrix[i:k, j:l]

    submatrices = []
    for submatrix in all_submatrices(matrix):
        if np.sum(submatrix) == 13:
            submatrices.append(submatrix.tolist())

    return submatrices
