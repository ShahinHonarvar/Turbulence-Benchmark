
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for sub_row in range(1, n_rows + 1):
        for sub_col in range(1, n_cols + 1):
            if sub_row * sub_col == 91:
                count += (n_rows - sub_row + 1) * (n_cols - sub_col + 1)
    return count
