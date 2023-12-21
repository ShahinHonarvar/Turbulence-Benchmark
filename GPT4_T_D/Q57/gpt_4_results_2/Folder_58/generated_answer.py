
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    
    for start_row in range(rows):
        for end_row in range(start_row + 1, rows + 1):
            for start_col in range(cols):
                for end_col in range(start_col + 1, cols + 1):
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if np.sum(submatrix) == -137:
                        submatrices.append(submatrix.tolist())
                        
    return submatrices
