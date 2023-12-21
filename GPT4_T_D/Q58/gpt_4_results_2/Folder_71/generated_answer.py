
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_len, col_len = matrix.shape
    for sub_row in range(1, row_len+1):
        for sub_col in range(1, col_len+1):
            for row in range(row_len-sub_row+1):
                for col in range(col_len-sub_col+1):
                    if sub_row*sub_col == 78:
                        count += 1
    return count
