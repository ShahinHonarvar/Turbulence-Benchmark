
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    
    for r_start in range(rows):
        for r_end in range(r_start, rows):
            for c_start in range(cols):
                for c_end in range(c_start, cols):
                    submatrix = matrix[r_start:r_end+1, c_start:c_end+1]
                    if np.sum(submatrix) == 1:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
