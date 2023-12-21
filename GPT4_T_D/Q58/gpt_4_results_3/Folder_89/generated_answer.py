
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_row in range(1, rows+1):
        for sub_col in range(1, cols+1):
            if sub_row * sub_col == 18:
                count += (rows - sub_row + 1) * (cols - sub_col + 1)
    return count
