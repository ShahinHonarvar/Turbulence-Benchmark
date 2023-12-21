
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for row_left in range(rows):
        for row_right in range(row_left + 1, rows + 1):
            for col_left in range(cols):
                for col_right in range(col_left + 1, cols + 1):
                    submatrix = matrix[row_left:row_right, col_left:col_right]
                    if np.sum(submatrix) == 2:
                        submatrices.append(submatrix)

    return submatrices
