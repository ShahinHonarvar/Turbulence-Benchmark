
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    output = []
    
    for sub_mat_cols in range(1, cols + 1):
        for sub_mat_rows in range(1, rows + 1):
            for row in range(rows - sub_mat_rows + 1):
                for col in range(cols - sub_mat_cols + 1):
                    submatrix = matrix[row:row + sub_mat_rows, col:col + sub_mat_cols]
                    if np.sum(submatrix) == -47:
                        output.append(submatrix)
    return output
