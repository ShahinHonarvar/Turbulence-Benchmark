
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for sub_matrix_rows in range(1, rows+1):
        for sub_matrix_columns in range(1, columns+1):
            if sub_matrix_rows*sub_matrix_columns == 29:
                count += (rows - sub_matrix_rows + 1) * (columns - sub_matrix_columns + 1)
    return count
