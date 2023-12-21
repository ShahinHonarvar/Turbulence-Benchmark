
import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    nrows, ncols = matrix.shape

    for row_size in range(1, nrows + 1):
        for col_size in range(1, ncols + 1):
            for start_row in range(nrows - row_size + 1):
                for start_col in range(ncols - col_size + 1):
                    sub_matrix = matrix[start_row:start_row+row_size,start_col:start_col+col_size]
                    if np.sum(sub_matrix) == -452:
                        output.append(sub_matrix)
    return output
