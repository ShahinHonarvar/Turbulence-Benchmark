
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for row in range(m):
        for col in range(n):
            for r in range(row+1, m+1):
                for c in range(col+1, n+1):
                    submatrix = matrix[row:r, col:c]
                    if np.sum(submatrix) == -308:
                        submatrices.append(submatrix)
    return submatrices
