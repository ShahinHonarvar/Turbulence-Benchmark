
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for row_size in range(1, rows+1):
        for column_size in range(1, columns+1):
            for row in range(rows - row_size + 1):
                for column in range(columns - column_size + 1):
                    submatrix_size = row_size * column_size
                    if submatrix_size == 118:
                        count += 1
    return count
