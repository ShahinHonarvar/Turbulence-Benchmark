
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    num_rows, num_cols = matrix.shape
    for row in range(num_rows):
        for col in range(num_cols):
            for sub_mat_rows in range(row+1, num_rows+1):
                for sub_mat_cols in range(col+1, num_cols+1):
                    submatrix = matrix[row:sub_mat_rows, col:sub_mat_cols]
                    if np.sum(submatrix) == -63:
                        result.append(submatrix)
    return result
