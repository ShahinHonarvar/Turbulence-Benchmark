
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    submatrices = []

    for row_size in range(1, rows+1):
        for col_size in range(1, cols+1):
            for r in range(rows - row_size + 1):
                for c in range(cols - col_size + 1):
                    submatrix = matrix[r:r+row_size, c:c+col_size]
                    if np.sum(submatrix) == -25:
                        submatrices.append(submatrix)

    return submatrices
