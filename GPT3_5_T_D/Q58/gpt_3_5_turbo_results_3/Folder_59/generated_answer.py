
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r, c] == 76:
                for i in range(r, rows):
                    for j in range(c, cols):
                        if np.sum(matrix[r:i+1, c:j+1]) == 76:
                            count += 1
    return count
