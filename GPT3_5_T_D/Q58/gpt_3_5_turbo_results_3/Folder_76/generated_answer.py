
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    
    for r in range(0, rows-1):
        for c in range(0, cols-1):
            if matrix[r][c] == 159:
                sub_matrix = matrix[r:r+2, c:c+2]
                if np.sum(sub_matrix) == 159:
                    count += 1
    
    return count
