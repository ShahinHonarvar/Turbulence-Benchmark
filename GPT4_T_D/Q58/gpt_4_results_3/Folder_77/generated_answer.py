
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for row_i in range(rows):
        for row_j in range(row_i + 1, rows + 1):
            for col_i in range(cols):
                for col_j in range(col_i + 1, cols + 1):
                    submatrix = matrix[row_i:row_j, col_i:col_j]
                    if submatrix.size == 179:
                        count += 1

    return count
