
import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrix_list = []
    row_len, col_len = np.shape(matrix)
    # Find all submatrices
    for sub_row_len in range(1, row_len+1):
        for sub_col_len in range(1, col_len+1):
            for i in range(row_len+1-sub_row_len):
                for j in range(col_len+1-sub_col_len):
                    sub_matrix = matrix[i:i+sub_row_len, j:j+sub_col_len]
                    if np.sum(sub_matrix) == 28:
                        sub_matrix_list.append(sub_matrix)
    return sub_matrix_list
