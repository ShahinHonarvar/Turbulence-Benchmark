
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = np.shape(matrix)
    
    for r in range(rows):
        for c in range(cols):
            for row_size in range(1, rows-r+1):
                for col_size in range(1, cols-c+1):
                    submatrix = matrix[r:(r+row_size), c:(c+col_size)]
                    if np.sum(submatrix) == 411:
                        submatrices.append(submatrix)
                        
    return submatrices
