
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 121
    rows, cols = matrix.shape
    
    for i in range(rows - 10):
        for j in range(cols - 10):
            submatrix = matrix[i:i+11, j:j+11]
            if np.sum(submatrix) == n:
                count += 1
    
    return count
