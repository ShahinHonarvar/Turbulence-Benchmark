
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 34
    rows, cols = matrix.shape
    count = 0
    
    for r in range(rows - n + 1):
        for c in range(cols - n + 1):
            submatrix = matrix[r:r+n, c:c+n]
            if np.all(submatrix == n):
                count += 1
    
    return count
