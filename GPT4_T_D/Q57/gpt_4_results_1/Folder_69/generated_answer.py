
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for row_size in range(1, rows + 1): # the size of row of submatrix
        for col_size in range(1, cols + 1): # the size of column of submatrix
            for i in range(rows - row_size + 1): # the start row of submatrix
                for j in range(cols - col_size + 1): # the start column of submatrix
                    submatrix = matrix[i:i+row_size, j:j+col_size]
                    if np.sum(submatrix) == 752:
                        result.append(submatrix.tolist())
    return result
