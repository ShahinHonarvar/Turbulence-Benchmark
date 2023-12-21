
import numpy as np

def submatrix_with_n_numbers(matrix):
    row_size, col_size = matrix.shape
    count = 0
    for row_sub_size in range(1, row_size + 1):
        for col_sub_size in range(1, col_size + 1):
            for row_start in range(row_size - row_sub_size + 1):
                for col_start in range(col_size - col_sub_size + 1):
                    if row_sub_size * col_sub_size == 78:
                        count += 1
    return count
