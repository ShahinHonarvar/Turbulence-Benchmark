
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    row, col = matrix.shape
    target_sum = 66
    
    for start_row in range(row):
        for start_col in range(col):
            for end_row in range(start_row, row):
                for end_col in range(start_col, col):
                    submatrix = matrix[start_row:end_row+1, start_col:end_col+1]
                    if np.sum(submatrix) == target_sum:
                        result.append(submatrix.tolist())
    
    return result
