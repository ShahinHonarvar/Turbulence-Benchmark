
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for row_size in range(1, rows - start_row + 1):
                for col_size in range(1, cols - start_col + 1):
                    submatrix = matrix[start_row : start_row + row_size, start_col : start_col + col_size]
                    if submatrix.size == 159:
                        count += 1
    return count
