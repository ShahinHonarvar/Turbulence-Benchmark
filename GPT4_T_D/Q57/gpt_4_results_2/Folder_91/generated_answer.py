
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for sub_mat_rows in range(1, rows + 1):
        for sub_mat_cols in range(1, cols + 1):
            for row in range(0, rows - sub_mat_rows + 1):
                for col in range(0, cols - sub_mat_cols + 1):
                    sub_matrix = matrix[row:row+sub_mat_rows, col:col+sub_mat_cols]
                    if np.sum(sub_matrix) == -6:
                        result.append(sub_matrix)
    return result
