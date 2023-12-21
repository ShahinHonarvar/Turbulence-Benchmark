
import numpy as np

def submatrix_with_particular_sum(input_matrix):
    rows, cols = input_matrix.shape
    output_submatrices  = []
    for sub_matrix_row in range(1, rows+1):
        for sub_matrix_col in range(1, cols+1):
            for row in range(rows - sub_matrix_row + 1):
                for col in range(cols - sub_matrix_col + 1):
                    sub_matrix = input_matrix[row:row + sub_matrix_row, col:col + sub_matrix_col]
                    if np.sum(sub_matrix) == 15:
                        output_submatrices.append(sub_matrix.tolist())
    return output_submatrices
