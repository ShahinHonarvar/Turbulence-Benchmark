
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    k = 95
    submatrices = []
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row+1, rows+1):
                for sub_col in range(col+1, cols+1):
                    submatrix = matrix[row:sub_row, col:sub_col]
                    if np.sum(submatrix) == k:
                        submatrices.append(submatrix.tolist())
    return submatrices
