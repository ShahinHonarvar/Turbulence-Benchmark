
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row, col = matrix.shape
    
    for row_idx in range(row):
        for col_idx in range(col):
            for row_size in range(row_idx + 1, row + 1):
                for col_size in range(col_idx + 1, col + 1):
                    submatrix = matrix[row_idx:row_size, col_idx:col_size]
                    if np.sum(submatrix) == -93:
                        submatrices.append(submatrix)
                        
    return submatrices
