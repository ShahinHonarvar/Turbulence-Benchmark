
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for size_row in range(1, rows + 1):
        for size_col in range(1, cols + 1):
            for r in range(rows - size_row + 1):
                for c in range(cols - size_col + 1):
                    submatrix = matrix[r:r+size_row, c:c+size_col]
                    if np.sum(submatrix) == 84:
                        submatrices.append(submatrix.tolist())
    return submatrices
