
import numpy as np

def submatrix_with_n_numbers(two_dim_matrix):
    row, col = np.shape(two_dim_matrix)
    count = 0
    for submatrix_row in range(1, row + 1):
        for submatrix_col in range(1, col + 1):
            if submatrix_row * submatrix_col == 92:
                count += (row - submatrix_row + 1) * (col - submatrix_col + 1)
    return count
