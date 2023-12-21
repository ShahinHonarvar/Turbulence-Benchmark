
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    r, c = matrix.shape
    for size in range(1, min(r, c) + 1):
        for i in range(r - size + 1):
            for j in range(c - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.sum(submatrix) == -185:
                    submatrices.append(submatrix.tolist())
    return submatrices
