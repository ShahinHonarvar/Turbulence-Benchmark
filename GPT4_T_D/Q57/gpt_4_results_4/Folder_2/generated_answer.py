
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for start_row in range(nrows):
        for start_col in range(ncols):
            for end_row in range(start_row + 1, nrows + 1):
                for end_col in range(start_col + 1, ncols + 1):
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if submatrix.sum() == -863:
                        submatrices.append(submatrix)
    return submatrices
