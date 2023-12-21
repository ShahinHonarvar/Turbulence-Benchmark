
import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    sub_matrix_list = []
    
    for sub_row in range(1, row + 1):
        for sub_col in range(1, col + 1):
            for start_row in range(row + 1 - sub_row):
                for start_col in range(col + 1 - sub_col):
                    sub_matrix = matrix[start_row:(start_row + sub_row), start_col:(start_col + sub_col)]
                    if np.sum(sub_matrix) == -64:
                        sub_matrix_list.append(sub_matrix)
                        
    return sub_matrix_list
