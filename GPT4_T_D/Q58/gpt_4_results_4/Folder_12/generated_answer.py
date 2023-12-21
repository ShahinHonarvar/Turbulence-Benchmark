
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = np.shape(matrix)
    count = 0

    for row_submatrix in range(1, row+1):
        for col_submatrix in range(1, col+1):
            if row_submatrix * col_submatrix == 46:
                count += (row - row_submatrix + 1) * (col - col_submatrix + 1)

    return count
