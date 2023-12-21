
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_size in range(1, rows + 1):
        for col_size in range(1, cols + 1):
            for row in range(rows - row_size + 1):
                for col in range(cols - col_size + 1):
                    if row_size * col_size == 159:
                        count += 1
    return count
