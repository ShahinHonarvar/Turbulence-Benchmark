
import numpy as np

def submatrix_with_n_numbers(matrix):
    num = 0
    rows, cols = matrix.shape
    for sub_matrix_rows in range(1, rows+1):
        for sub_matrix_cols in range(1, cols+1):
            if sub_matrix_rows * sub_matrix_cols == 20:
                num += (rows - sub_matrix_rows + 1) * (cols - sub_matrix_cols + 1)
    return num
