
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            if sub_rows * sub_cols == 18:
                count += (rows - sub_rows + 1) * (cols - sub_cols + 1)
    return count
