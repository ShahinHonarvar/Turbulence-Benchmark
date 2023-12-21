
import numpy as np

def submatrix_with_n_numbers(mat):
    row, col = mat.shape
    count = 0

    # check submatrices count with 146 integers
    for size_row in range(1, row + 1):
        for size_col in range(1, col + 1):
            for sub_row_start in range(0, row - size_row + 1):
                for sub_col_start in range(0, col - size_col + 1):
                    submat = mat[sub_row_start:sub_row_start + size_row, sub_col_start:sub_col_start + size_col]
                    if submat.size == 146:
                        count += 1

    return count
