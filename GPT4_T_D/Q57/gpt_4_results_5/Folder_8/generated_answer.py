
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row = matrix.shape[0]
    col = matrix.shape[1]
    for size_row in range(1, row + 1):
        for size_col in range(1, col + 1):
            for r in range(0, row - size_row + 1):
                for c in range(0, col - size_col + 1):
                    submatrix = matrix[r:r+size_row, c:c+size_col]
                    if np.sum(submatrix) == -61:
                        submatrices.append(submatrix)
    return submatrices
