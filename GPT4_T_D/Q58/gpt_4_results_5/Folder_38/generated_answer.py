
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows_len = len(matrix)
    cols_len = len(matrix[0]) if rows_len else 0

    for i in range(rows_len):
        for j in range(cols_len):
            for p in range(i, rows_len):
                for q in range(j, cols_len):
                    submatrix = matrix[i:p+1, j:q+1]
                    if submatrix.size == 34:
                        count += 1
    return count
