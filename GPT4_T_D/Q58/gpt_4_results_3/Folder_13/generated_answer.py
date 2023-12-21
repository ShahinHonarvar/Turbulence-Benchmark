
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape[0], mat.shape[1]
    
    for r_dim in range(1, rows + 1):
        for c_dim in range(1, cols + 1):
            if r_dim * c_dim == 175:
                for x in range(rows - r_dim + 1):
                    for y in range(cols - c_dim + 1):
                        count += 1
                        
    return count
