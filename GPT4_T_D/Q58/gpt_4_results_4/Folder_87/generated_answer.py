
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for submatrix_row in range(1, rows + 1):
        for submatrix_col in range(1, columns + 1):
            if(submatrix_row * submatrix_col == 96):
                count += (rows - submatrix_row + 1) * (columns - submatrix_col + 1)
    return count
