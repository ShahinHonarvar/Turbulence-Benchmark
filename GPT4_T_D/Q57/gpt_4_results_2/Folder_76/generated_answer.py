
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            for row in range(0, rows - sub_rows + 1):
                for col in range(0, cols - sub_cols + 1):
                    submatrix = matrix[row:row+sub_rows, col:col+sub_cols]
                    if submatrix.sum() == -255:
                        submatrices.append(submatrix)
    return submatrices
