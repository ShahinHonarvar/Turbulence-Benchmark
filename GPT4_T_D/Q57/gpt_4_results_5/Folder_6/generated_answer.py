
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for sub_m in range(m):
        for sub_n in range(n):
            for r in range(sub_m, m):
                for c in range(sub_n, n):
                    submatrix = matrix[sub_m:r+1, sub_n:c+1]
                    if np.sum(submatrix) == 126:
                        submatrices.append(submatrix)
    return submatrices
