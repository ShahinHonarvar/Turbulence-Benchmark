
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    sub_matrix = matrix[start_row:end_row+1, start_col:end_col+1]
                    if np.sum(sub_matrix) == -10:
                        sub_matrices.append(sub_matrix.tolist())
    return sub_matrices
