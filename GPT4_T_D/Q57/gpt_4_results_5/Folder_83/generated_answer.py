
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row, rows):
                for sub_col in range(col, cols):
                    submatrix = matrix[row:sub_row+1, col:sub_col+1]
                    if np.sum(submatrix) == -15:
                        submatrices.append(submatrix)
    return submatrices
