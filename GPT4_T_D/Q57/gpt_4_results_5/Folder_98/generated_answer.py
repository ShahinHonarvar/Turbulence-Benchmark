
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_sum_submatrices = []
    
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    submatrix = matrix[start_row:end_row+1, start_col:end_col+1]
                    if np.sum(submatrix) == 0:
                        zero_sum_submatrices.append(submatrix.tolist())
    
    return zero_sum_submatrices
