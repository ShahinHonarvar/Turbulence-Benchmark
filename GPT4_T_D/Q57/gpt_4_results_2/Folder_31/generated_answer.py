
import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    submatrices = []

    for row_size in range(1, row + 1):
        for col_size in range(1, col + 1):
            for r in range(row - row_size + 1):
                for c in range(col - col_size + 1):
                    submatrix = matrix[r:r+row_size, c:c+col_size]
                    if np.sum(submatrix) == -44:
                        submatrices.append(submatrix)
                   
    return submatrices
