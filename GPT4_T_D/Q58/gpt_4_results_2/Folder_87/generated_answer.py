
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row_length in range(1, rows+1):
        for col_length in range(1, cols+1):
            if row_length * col_length == 96:
                count += (rows - row_length + 1) * (cols - col_length + 1)
    return count
