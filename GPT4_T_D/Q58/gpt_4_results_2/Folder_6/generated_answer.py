
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_count = 0
    for sub_rows in range(rows):
        for sub_cols in range(cols):
            for r in range(rows - sub_rows + 1):
                for c in range(cols - sub_cols + 1):
                    submatrix = matrix[r:r + sub_rows, c:c + sub_cols]
                    if submatrix.size == 122:
                        submatrix_count += 1
    return submatrix_count
