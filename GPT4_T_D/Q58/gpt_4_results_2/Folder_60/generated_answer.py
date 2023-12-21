
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for row_start in range(rows):
        for col_start in range(columns):
            for row_end in range(row_start + 1, rows + 1):
                for col_end in range(col_start + 1, columns + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.size(submatrix) == 88:
                        count += 1
    return count
