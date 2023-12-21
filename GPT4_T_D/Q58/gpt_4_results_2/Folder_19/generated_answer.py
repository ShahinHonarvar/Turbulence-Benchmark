
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for sub_rows in range(1, rows+1):
        for sub_columns in range(1, columns+1):
            if sub_rows*sub_columns == 17:
                count += (rows - sub_rows + 1) * (columns - sub_columns + 1)
    return count
