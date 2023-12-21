
import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrix_list = []
    rows, cols = matrix.shape
    for sub_row in range(1, rows+1):
        for sub_col in range(1, cols+1):
            for row in range(0, rows-sub_row+1):
                for col in range(0, cols-sub_col+1):
                    sub_matrix = matrix[row:row+sub_row, col:col+sub_col]
                    if np.sum(sub_matrix) == 66:
                        sub_matrix_list.append(sub_matrix)
    return sub_matrix_list
