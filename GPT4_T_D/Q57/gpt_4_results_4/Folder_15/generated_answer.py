
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.sum(submatrix) == -9:
                    submatrices.append(submatrix)
    return submatrices
