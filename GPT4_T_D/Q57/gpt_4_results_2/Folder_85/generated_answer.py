
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    nrows, ncols = matrix.shape
    for row in range(nrows):
        for col in range(ncols):
            for sub_row in range(row+1, nrows+1):
                for sub_col in range(col+1, ncols+1):
                    submatrix = matrix[row:sub_row, col:sub_col]
                    if np.sum(submatrix) == -87:
                        result.append(submatrix)
    return result
