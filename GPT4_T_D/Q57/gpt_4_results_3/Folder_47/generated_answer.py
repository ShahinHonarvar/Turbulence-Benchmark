
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[0], matrix.shape[1]
    submatrices = []

    for submatrix_size in range(1, min(rows, cols) + 1):
        for r in range(0, rows - submatrix_size + 1):
            for c in range(0, cols - submatrix_size + 1):
                submatrix = matrix[r:r+submatrix_size, c:c+submatrix_size]
                if np.sum(submatrix) == 27:
                    submatrices.append(submatrix)
    return submatrices
