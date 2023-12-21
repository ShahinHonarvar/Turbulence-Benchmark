
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    submatrix = matrix[start_row:end_row+1, start_col:end_col+1]
                    if submatrix.size == 64:
                        count += 1
                        
    return count
