
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    max_row, max_col = rows - 85 + 1, cols - 85 + 1

    for i in range(max_row):
        for j in range(max_col):
            submatrix = matrix[i:i+85, j:j+85]
            if np.sum(submatrix) == 85 * 85:
                count += 1

    return count
