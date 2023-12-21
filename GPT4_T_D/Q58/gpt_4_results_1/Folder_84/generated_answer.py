
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row_idx in range(rows):
        for col_idx in range(cols):
            for end_row in range(row_idx+1, rows+1):
                for end_col in range(col_idx+1, cols+1):
                    sub_matrix = matrix[row_idx:end_row, col_idx:end_col]
                    if sub_matrix.size == 127:
                        count += 1
    return count
