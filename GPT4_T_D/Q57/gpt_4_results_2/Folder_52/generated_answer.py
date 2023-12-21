
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for row in range(nrows+1):
        for col in range(ncols+1):
            for sub_row in range(row+1, nrows+1):
                for sub_col in range(col+1, ncols+1):
                    submatrix = matrix[row:sub_row, col:sub_col]
                    sum_of_elements = np.sum(submatrix)
                    if sum_of_elements == 100:
                        result.append(submatrix)
    return result
