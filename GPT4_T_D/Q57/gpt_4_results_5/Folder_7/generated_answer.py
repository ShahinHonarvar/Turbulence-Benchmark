
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    submatrices = []
    
    for s_row in range(rows):
        for s_col in range(cols):
            for e_row in range(s_row+1, rows+1):
                for e_col in range(s_col+1, cols+1):
                    submatrix = matrix[s_row:e_row, s_col:e_col]
                    if np.sum(submatrix) == -128:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
