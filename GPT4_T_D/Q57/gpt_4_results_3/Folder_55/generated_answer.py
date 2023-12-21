
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape

    for row in range(rows):
        for col in range(cols):
            for row_length in range(1, rows+1):
                for col_length in range(1, cols+1):
                    if row + row_length > rows or col + col_length > cols:
                        continue
                    submatrix = matrix[row:row+row_length, col:col+col_length]
                    if np.sum(submatrix) == 1:
                        result.append(submatrix)

    return result
