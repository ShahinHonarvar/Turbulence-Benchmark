
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    submatrix = matrix[start_row:end_row+1, start_col:end_col+1]
                    if np.sum(submatrix) == 97:
                        count += 1
    return count
