
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for start_row in range(rows):
        for end_row in range(start_row, rows):
            for start_col in range(cols):
                for end_col in range(start_col, cols):
                    sub_matrix = matrix[start_row:end_row+1, start_col:end_col+1]
                    if np.sum(sub_matrix) == 47:
                        count += 1
    return count
