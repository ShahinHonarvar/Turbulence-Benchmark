
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for row_count in range(1, rows + 1):
        for column_count in range(1, columns + 1):
            if row_count * column_count == 154:
                count += (rows - row_count + 1) * (columns - column_count + 1)
    return count
