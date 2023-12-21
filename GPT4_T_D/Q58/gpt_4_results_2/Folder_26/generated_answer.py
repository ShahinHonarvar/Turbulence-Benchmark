
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for row_length in range(1, rows + 1):
        for column_length in range(1, columns + 1):
            for r in range(rows - row_length + 1):
                for c in range(columns - column_length + 1):
                    submatrix = matrix[r:r+row_length, c:c+column_length]
                    if submatrix.size == 115:
                        count += 1
    return count
