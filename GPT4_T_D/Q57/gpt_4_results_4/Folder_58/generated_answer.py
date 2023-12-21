
import numpy as np

def submatrix_with_particular_sum(matrix):
    num_rows, num_cols = np.shape(matrix)
    submatrix_list = []
    
    for start_row in range(num_rows):
        for end_row in range(start_row+1, num_rows+1):
            for start_col in range(num_cols):
                for end_col in range(start_col+1, num_cols+1):
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if np.sum(submatrix) == -137:
                        submatrix_list.append(submatrix)
    
    return submatrix_list
