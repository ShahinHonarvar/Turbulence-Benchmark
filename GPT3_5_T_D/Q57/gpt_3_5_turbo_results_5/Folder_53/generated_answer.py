
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n_rows, n_cols = matrix.shape

    for start_row in range(n_rows):
        for start_col in range(n_cols):
            for end_row in range(start_row, n_rows):
                for end_col in range(start_col, n_cols):
                    submatrix = matrix[start_row:end_row+1, start_col:end_col+1]
                    if np.sum(submatrix) == -37:
                        submatrices.append(submatrix.tolist())

    return submatrices
