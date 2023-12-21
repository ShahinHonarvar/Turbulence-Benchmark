
import numpy as np

def submatrix_with_n_numbers(input_matrix):
    count = 0
    rows, cols = input_matrix.shape
    for row_len in range(1, rows + 1):
        for col_len in range(1, cols + 1):
            for i in range(0, rows - row_len + 1):
                for j in range(0, cols - col_len + 1):
                    if row_len * col_len == 83:
                        count += 1
    return count
