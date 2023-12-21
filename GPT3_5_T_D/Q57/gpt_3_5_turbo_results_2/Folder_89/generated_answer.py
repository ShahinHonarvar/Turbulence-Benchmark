
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape

    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k+1, j:l+1]
                    if submatrix.sum() == 80:
                        submatrices.append(submatrix.tolist())

    return submatrices
