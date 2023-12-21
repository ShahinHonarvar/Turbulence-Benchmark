
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 19
    rows, cols = matrix.shape
    count = 0
    
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submat = matrix[i:i+n, j:j+n]
            if np.count_nonzero(submat == 1) == n:
                count += 1
    
    return count
