
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for x in range(n):
        for y in range(m):
            for r in range(x+1, n+1):
                for s in range(y+1, m+1):
                    submatrix = matrix[x:r, y:s]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == -38:
                        submatrices.append(submatrix.tolist())
    return submatrices
