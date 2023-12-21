
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for sub_row in range(1, row+1):
        for sub_col in range(1, col+1):
            if sub_row * sub_col == 74:
                count += (row - sub_row + 1) * (col - sub_col + 1)
    return count
