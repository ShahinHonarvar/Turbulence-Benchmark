
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    for i in range(n-1):
        for j in range(m-1):
            submatrices = []
            for k in range(i+1, n):
                for l in range(j+1, m):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == -20:
                        submatrices.append(submatrix)
            if len(submatrices) > 0:
                return submatrices
    return []
