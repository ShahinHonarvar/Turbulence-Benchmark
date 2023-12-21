
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[0], matrix.shape[1]
    submatrices = []
    for sub_matrix_row in range(1,rows+1):
        for sub_matrix_col in range(1,cols+1):
            for i in range(rows+1-sub_matrix_row):
                for j in range(cols+1-sub_matrix_col):
                    sub_matrix = matrix[i:i+sub_matrix_row, j:j+sub_matrix_col]
                    if np.sum(sub_matrix) == 38:
                        submatrices.append(sub_matrix.tolist())
    return submatrices
