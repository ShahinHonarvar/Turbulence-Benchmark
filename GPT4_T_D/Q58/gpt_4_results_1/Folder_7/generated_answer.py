
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            for row in range(rows - sub_rows + 1):
                for col in range(cols - sub_cols + 1):
                    submatrix = matrix[row:row + sub_rows, col:col + sub_cols]
                    if np.size(submatrix) == 121:
                        count += 1
    return count
