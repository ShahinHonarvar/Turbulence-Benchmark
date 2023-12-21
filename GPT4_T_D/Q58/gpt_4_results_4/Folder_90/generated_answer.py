
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for submat_row in range(1, rows + 1):
        for submat_col in range(1, cols + 1):
            if submat_row * submat_col == 176:
                count += (rows - submat_row + 1) * (cols - submat_col + 1)
    return count
