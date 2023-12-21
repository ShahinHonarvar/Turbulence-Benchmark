
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for sub_matrix_size_rows in range(1, rows+1):
        for sub_matrix_size_cols in range(1, cols+1):
            for i in range(0, rows - sub_matrix_size_rows + 1):
                for j in range(0, cols - sub_matrix_size_cols + 1):
                    submatrix = matrix[i:i+sub_matrix_size_rows,j:j+sub_matrix_size_cols]
                    if np.sum(submatrix) == 88:
                        submatrices.append(submatrix)
    return submatrices
