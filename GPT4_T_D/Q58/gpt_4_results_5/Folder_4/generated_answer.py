
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for src_row in range(rows):
        for src_col in range(cols):
            for dest_row in range(src_row, rows):
                for dest_col in range(src_col, cols):
                    submatrix = matrix[src_row:dest_row+1, src_col:dest_col+1]
                    if submatrix.size == 15:
                        count += 1
    return count
