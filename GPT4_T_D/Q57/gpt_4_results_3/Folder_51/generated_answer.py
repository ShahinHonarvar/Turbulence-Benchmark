
import numpy as np

def submatrix_with_particular_sum(matrix):
    end_list = []
    rows, cols = matrix.shape
    
    for row_size in range(1, rows+1):
        for col_size in range(1, cols+1):
            for row_start in range(rows-row_size+1):
                for col_start in range(cols-col_size+1):
                    submatrix = matrix[row_start:row_start+row_size, col_start:col_start+col_size]
                    if np.sum(submatrix) == -46:
                        end_list.append(submatrix)
                        
    return end_list
