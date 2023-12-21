
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_rows, num_cols = matrix.shape
    for submatrix_row in range(1, num_rows+1):
        for submatrix_col in range(1, num_cols+1):
            if submatrix_row * submatrix_col == 10:
                count += (num_rows - submatrix_row + 1) * (num_cols - submatrix_col + 1)
    return count
