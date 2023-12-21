
import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    
    for r1 in range(num_rows):
        for c1 in range(num_cols):
            for r2 in range(r1, num_rows):
                for c2 in range(c1, num_cols):
                    submatrix = matrix[r1:r2+1, c1:c2+1]
                    if submatrix.size == 21:
                        count += 1
                        
    return count
