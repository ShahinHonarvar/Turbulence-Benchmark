
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for submatrix_row in range(1, rows + 1):
        for submatrix_col in range(1, cols + 1):
            if submatrix_row * submatrix_col == 5:
                count += (rows - submatrix_row + 1) * (cols - submatrix_col + 1)
    return count
