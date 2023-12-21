
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_row in range(row, rows):
                for sub_col in range(col, cols):
                    submatrix = matrix[row:sub_row+1, col:sub_col+1]
                    if submatrix.size == 131:
                        count += 1
    return count
