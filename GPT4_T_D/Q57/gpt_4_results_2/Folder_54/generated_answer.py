
import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    submatrices = []
    for size in range(1, min(row, col) + 1):
        for i in range(row - size + 1):
            for j in range(col - size + 1):
                submatrix = matrix[i : i + size, j : j + size]
                if np.sum(submatrix) == -59:
                    submatrices.append(submatrix.tolist())
    return submatrices
