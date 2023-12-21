
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for window_row in range(row, rows):
                for window_col in range(col, cols):
                    submatrix = matrix[row:window_row+1, col:window_col+1]
                    if submatrix.size == 63:
                        count += 1
    return count
