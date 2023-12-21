
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, column = matrix.shape
    count = 0
    for row_sub in range(1, row + 1):
        for column_sub in range(1, column + 1):
            if row_sub * column_sub == 186:
                count += (row - row_sub + 1) * (column - column_sub + 1)
    return count
