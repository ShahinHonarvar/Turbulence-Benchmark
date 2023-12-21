
import numpy as np

def submatrix_with_particular_sum(matrix):
    output = []
    row_len, col_len = matrix.shape
    for row in range(row_len):
        for col in range(col_len):
            for delta_row in range(row_len - row + 1):
                for delta_col in range(col_len - col + 1):
                    submatrix = matrix[row:row+delta_row, col:col+delta_col]
                    if np.sum(submatrix) == -65:
                        output.append(submatrix)
    return output
