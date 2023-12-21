
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for sub_matrix_row in range(1, rows + 1):
        for sub_matrix_col in range(1, cols + 1):
            for row in range(rows - sub_matrix_row + 1):
                for col in range(cols - sub_matrix_col + 1):
                    submatrix = matrix[row : row + sub_matrix_row, col : col + sub_matrix_col]
                    if np.sum(submatrix) == 93:
                        submatrices.append(submatrix)
    return submatrices
