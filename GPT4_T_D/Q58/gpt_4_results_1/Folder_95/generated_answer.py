
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for row_len in range(1, rows + 1):
        for col_len in range(1, columns + 1):
            total_elements = row_len * col_len
            if total_elements == 87:
                count += (rows - row_len + 1) * (columns - col_len + 1)
    return count
