
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_length, col_length = matrix.shape
    for row_size in range(1, row_length + 1):
        for col_size in range(1, col_length + 1):
            for row in range(row_length - row_size + 1):
                for col in range(col_length - col_size + 1):
                    if row_size * col_size == 166:
                        count += 1
    return count
