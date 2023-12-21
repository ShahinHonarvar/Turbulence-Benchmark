
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(1, n-i+1):
                for l in range(1, m-j+1):
                    submatrix = matrix[i:i+k, j:j+l]
                    if np.sum(submatrix) == 21:
                        submatrices.append(submatrix.tolist())
    return submatrices
