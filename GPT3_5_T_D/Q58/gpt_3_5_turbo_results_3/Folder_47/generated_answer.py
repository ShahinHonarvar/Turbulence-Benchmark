
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    
    for i in range(rows - 9):
        for j in range(cols - 9):
            submatrix = matrix[i:i+9, j:j+9]
            
            if np.prod(submatrix.shape) == 90:
                count += 1
    
    return count if count > 0 else 0
