
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_rows, num_cols = matrix.shape
    for start_row in range(num_rows):
        for start_col in range(num_cols):
            for end_row in range(start_row, num_rows):
                for end_col in range(start_col, num_cols):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if np.sum(submatrix) == 154 * submatrix.size:
                        count += 1
    return count
