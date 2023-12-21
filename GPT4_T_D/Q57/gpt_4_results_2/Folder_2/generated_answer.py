
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    m, n = matrix.shape
    for submatrix_m in range(m+1):
        for submatrix_n in range(n+1):
            for i in range(m-submatrix_m+1):
                for j in range(n-submatrix_n+1):
                    submatrix = matrix[i:i+submatrix_m, j:j+submatrix_n]
                    if np.sum(submatrix) == -863:
                        submatrices.append(submatrix.tolist())
    return submatrices
