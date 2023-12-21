
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for r in range(rows-2):
        for c in range(cols-2):
            submatrix = matrix[r:r+3, c:c+3]
            if np.count_nonzero(submatrix) == 9:
                count += 1
    
    return count
