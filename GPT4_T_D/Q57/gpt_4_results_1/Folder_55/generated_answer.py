
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for sub_matrix_rows in range(1, rows + 1):
        for sub_matrix_cols in range(1, cols + 1):
            for r in range(rows - sub_matrix_rows + 1):
                for c in range(cols - sub_matrix_cols + 1):
                    sub_matrix = matrix[r:r + sub_matrix_rows, c:c + sub_matrix_cols]
                    if np.sum(sub_matrix) == 1:
                        result.append(sub_matrix)
    return result
