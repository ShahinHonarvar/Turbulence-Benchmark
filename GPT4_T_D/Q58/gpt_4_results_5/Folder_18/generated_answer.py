
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_size in range(1, rows+1):
        for col_size in range(1, cols+1):
            submatrices_in_row = rows - row_size + 1
            submatrices_in_col = cols - col_size + 1
            total_submatrices = submatrices_in_row * submatrices_in_col
            if row_size*col_size == 104:
                count += total_submatrices
    return count
