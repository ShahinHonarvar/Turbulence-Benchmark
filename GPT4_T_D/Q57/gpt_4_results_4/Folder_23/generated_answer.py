
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for submatrix_row_size in range(1, rows+1):
        for submatrix_col_size in range(1, cols+1):
            for row in range(0, rows-submatrix_row_size+1):
                for col in range(0, cols-submatrix_col_size+1):
                    submatrix = matrix[row:row+submatrix_row_size, col:col+submatrix_col_size]
                    if np.sum(submatrix) == 59:
                        result.append(submatrix)
    return result
