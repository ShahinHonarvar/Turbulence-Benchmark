
import numpy as np

def submatrix_with_n_numbers(matrix):
    matrices_count = 0
    rows, cols = matrix.shape
    for row_end in range(rows):
        for col_end in range(cols):
            for row_start in range(row_end + 1):
                for col_start in range(col_end + 1):
                    if (row_end - row_start + 1) * (col_end - col_start + 1) == 144:
                        matrices_count += 1
    return matrices_count
