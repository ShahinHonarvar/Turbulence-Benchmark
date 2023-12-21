
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    rows, cols = matrix.shape
    count = 0
    
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if len(set(matrix[i:i+n, j:j+n].flatten())) == n:
                count += 1
                
    return count
