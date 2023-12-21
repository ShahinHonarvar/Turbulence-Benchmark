
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for size in range(1, min(m, n) + 1):
        for x in range(m - size + 1):
            for y in range(n - size + 1):
                submatrix = matrix[x:x+size, y:y+size]
                if np.sum(submatrix) == 59:
                    submatrices.append(submatrix)
    return submatrices
