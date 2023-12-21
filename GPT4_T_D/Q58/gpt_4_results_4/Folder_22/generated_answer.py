
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for row_length in range(1, row + 1):
        for col_length in range(1, col + 1):
            if row_length * col_length == 21:
                for i in range(0, row - row_length + 1):
                    for j in range(0, col - col_length + 1):
                        count += 1
    return count
