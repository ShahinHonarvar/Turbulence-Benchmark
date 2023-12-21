
import numpy as np

def submatrix_with_particular_sum(matrix):
    def submatrix_sum(submatrix):
        return np.sum(submatrix)

    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k+1, j:l+1]
                    if submatrix_sum(submatrix) == 40:
                        submatrices.append(submatrix.tolist())

    return submatrices
