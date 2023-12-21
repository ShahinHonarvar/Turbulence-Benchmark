
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == -6:
                        submatrices.append(submatrix)
    return submatrices
