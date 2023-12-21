
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for r in range(rows - 1):
        for c in range(cols - 1):
            if matrix[r, c] == 91:
                if matrix[r + 1, c + 1] == 91:
                    count += 1
    
    return count
