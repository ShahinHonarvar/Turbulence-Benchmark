
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for start_row in range(row):
        for start_col in range(col):
            for end_row in range(start_row + 1, row + 1):
                for end_col in range(start_col + 1, col + 1):
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if submatrix.size == 47:
                        count += 1
    return count
