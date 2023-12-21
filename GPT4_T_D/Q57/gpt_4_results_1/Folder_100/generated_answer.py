
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for size in range(1, min(n, m) + 1):
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                submatrix = matrix[i:i+size,j:j+size]
                if np.sum(submatrix) == 28:
                    submatrices.append(submatrix)
    return submatrices
