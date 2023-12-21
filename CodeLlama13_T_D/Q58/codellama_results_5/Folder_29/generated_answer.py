
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    rows, cols = matrix.shape
    count = 0
    
    for row in range(rows-n+1):
        for col in range(cols-n+1):
            if np.sum(matrix[row:row+n, col:col+n]) == n**2:
                count += 1
                
    return count
