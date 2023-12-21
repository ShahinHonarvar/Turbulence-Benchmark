
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n = matrix.shape[0]
    m = matrix.shape[1]
    
    for submatrix_n in range(1, n+1):
        for submatrix_m in range(1, m+1):
            for i in range(n - submatrix_n + 1):
                for j in range(m - submatrix_m + 1):
                    submatrix = matrix[i:i+submatrix_n, j:j+submatrix_m]
                    if np.sum(submatrix) == -3:
                        submatrices.append(submatrix)
    return submatrices
