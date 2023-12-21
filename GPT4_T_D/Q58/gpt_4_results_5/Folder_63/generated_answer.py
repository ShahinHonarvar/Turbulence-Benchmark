
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for submatrix_rows in range(1, rows + 1):
        for submatrix_cols in range(1, cols + 1):
            for i in range(rows - submatrix_rows + 1):
                for j in range(cols - submatrix_cols + 1):
                    submatrix = matrix[i : i + submatrix_rows, j : j + submatrix_cols]
                    if submatrix.size == 57:
                        count += 1
    return count
