
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for submatrix_rows in range(1, rows + 1):
        for submatrix_cols in range(1, cols + 1):
            if submatrix_rows * submatrix_cols == 76:
                count += (rows - submatrix_rows + 1) * (cols - submatrix_cols + 1)
    return count
