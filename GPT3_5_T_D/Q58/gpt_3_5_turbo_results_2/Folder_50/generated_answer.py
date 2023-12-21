
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 40
    nrows, ncols = matrix.shape
    
    for i in range(nrows - n + 1):
        for j in range(ncols - n + 1):
            submatrix = matrix[i:i+n, j:j+n]
            if np.sum(submatrix) == n * n:
                count += 1
                
    return count
