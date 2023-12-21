
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start + 1, rows + 1):
                for col_end in range(col_start + 1, cols + 1):
                    sub_matrix = matrix[row_start:row_end, col_start:col_end]
                    if np.size(sub_matrix) == 27:
                        count += 1
    return count
