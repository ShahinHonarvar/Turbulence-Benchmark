
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for submatrix_rows in range(1, rows+1):
        for submatrix_columns in range(1, columns+1):
            if submatrix_rows * submatrix_columns == 99:
                count += (rows - submatrix_rows + 1) * (columns - submatrix_columns + 1)
    return count
