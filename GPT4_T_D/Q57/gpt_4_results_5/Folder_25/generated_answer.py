
import numpy as np

def submatrix_with_particular_sum(input_matrix):
    list_of_submatrix = []
    rows, cols = input_matrix.shape
    for row in range(rows):
        for col in range(cols):
            for sub_matrix_row in range(row+1, rows+1):
                for sub_matrix_col in range(col+1, cols+1):
                    sub_matrix = input_matrix[row:sub_matrix_row, col:sub_matrix_col]
                    if np.sum(sub_matrix) == -20:
                        list_of_submatrix.append(sub_matrix)
    return list_of_submatrix
