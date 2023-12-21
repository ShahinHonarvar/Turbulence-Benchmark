
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for top_row in range(0, rows):
        for left_col in range(0, cols):
            for bottom_row in range(top_row+1, rows+1):
                for right_col in range(left_col+1, cols+1):
                    submatrix = matrix[top_row:bottom_row, left_col:right_col]
                    if np.sum(submatrix) == -47:
                        submatrices.append(submatrix)
    return submatrices
