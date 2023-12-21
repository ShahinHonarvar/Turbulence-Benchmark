
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r, c] == 118:
                count += 1

    return count
