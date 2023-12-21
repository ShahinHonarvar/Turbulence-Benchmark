
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    sub_matrix_rows = k - i + 1
                    sub_matrix_cols = l - j + 1
                    if sub_matrix_rows * sub_matrix_cols == 8:
                        count += 1
    return count
