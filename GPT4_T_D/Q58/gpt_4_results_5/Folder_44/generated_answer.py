
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_ix in range(rows):
        for col_ix in range(cols):
            for row_len in range(1, rows - row_ix + 1):
                for col_len in range(1, cols - col_ix + 1):
                    submatrix = matrix[row_ix : row_ix+row_len, col_ix : col_ix+col_len]
                    if np.count_nonzero(submatrix == 191) == 191:
                        count += 1
    return count
