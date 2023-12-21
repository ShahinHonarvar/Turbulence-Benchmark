
import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for row1 in range(n_rows):
        for col1 in range(n_cols):
            for row2 in range(row1, n_rows):
                for col2 in range(col1, n_cols):
                    if (row2 - row1 + 1) * (col2 - col1 + 1) == 48:
                        count += 1
    return count
