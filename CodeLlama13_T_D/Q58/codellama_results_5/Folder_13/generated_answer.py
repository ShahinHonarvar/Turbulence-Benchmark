
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i+n, j:j+n]
            if np.count_nonzero(submatrix) == n**2:
                return True
    return False
