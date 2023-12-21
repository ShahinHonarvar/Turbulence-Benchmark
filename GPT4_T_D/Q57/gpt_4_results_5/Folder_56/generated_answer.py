
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    
    for row_size in range(1, rows+1):
        for col_size in range(1, cols+1):
            for i in range(rows - row_size + 1):
                for j in range(cols - col_size + 1):
                    submatrix = matrix[i:i+row_size, j:j+col_size]
                    if np.sum(submatrix) == -50:
                        submatrices.append(submatrix)
    
    return submatrices
