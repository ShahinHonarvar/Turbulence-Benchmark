
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]
    count = 0
    
    for row in range(num_rows - n + 1):
        for col in range(num_cols - n + 1):
            submatrix = matrix[row:row+n, col:col+n]
            if np.all(submatrix == 42):
                count += 1
                
    return count
