
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for sub_matrix_row in range(1, rows + 1):
        for sub_matrix_col in range(1, cols + 1):
            if sub_matrix_row * sub_matrix_col == 46:
                count += (rows - sub_matrix_row + 1) * (cols - sub_matrix_col + 1)
    return count
