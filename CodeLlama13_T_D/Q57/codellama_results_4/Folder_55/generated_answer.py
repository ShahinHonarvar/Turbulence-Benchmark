
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    
    for row in range(rows):
        for col in range(cols):
            submatrix = matrix[row:, col:]
            if np.sum(submatrix) == 1:
                result.append((row, col))
                
    return result
