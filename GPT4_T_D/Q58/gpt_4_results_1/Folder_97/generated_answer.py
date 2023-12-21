
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for size_row in range(row + 1, rows + 1):
                for size_col in range(col + 1, cols + 1):
                    submatrix = matrix[row:size_row, col:size_col]
                    if np.size(submatrix) == 120:
                        count += 1
    return count
