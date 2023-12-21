
import numpy as np

def submatrix_with_particular_sum(matrix):
    n_rows = matrix.shape[0]
    n_cols = matrix.shape[1]
    submatrices = []
    
    for row_size in range(1, n_rows+1):
        for col_size in range(1, n_cols+1):
            for row_start in range(n_rows-row_size+1):
                for col_start in range(n_cols-col_size+1):
                    submatrix = matrix[row_start:(row_start+row_size), col_start:(col_start+col_size)]
                    if np.sum(submatrix) == 88:
                        submatrices.append(submatrix)
                        
    return submatrices
