
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    target_sum = 382
    
    for top_left_row in range(rows):
        for top_left_col in range(cols):
            for bottom_right_row in range(top_left_row, rows):
                for bottom_right_col in range(top_left_col, cols):
                    submatrix = matrix[top_left_row:bottom_right_row+1, top_left_col:bottom_right_col+1]
                    
                    if np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
