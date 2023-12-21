
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for sub_row in range(rows+1):
        for sub_col in range(cols+1):
            for start_row in range(rows-sub_row+1):
                for start_col in range(cols-sub_col+1):
                    submatrix = matrix[start_row:start_row+sub_row, start_col:start_col+sub_col]
                    if submatrix.sum() == -4:
                        submatrices.append(submatrix)
    return submatrices
