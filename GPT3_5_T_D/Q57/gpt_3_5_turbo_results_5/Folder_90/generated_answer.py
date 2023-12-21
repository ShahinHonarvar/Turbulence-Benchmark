
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for p in range(i, m):
                for q in range(j, n):
                    submatrix = matrix[i:p+1, j:q+1]
                    if np.sum(submatrix) == -452:
                        submatrices.append(submatrix.tolist())
    return submatrices
