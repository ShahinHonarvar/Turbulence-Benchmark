
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    
    for r in range(rows):
        for c in range(cols):
            for ri in range(r+1, rows+1):
                for ci in range(c+1, cols+1):
                    submatrix = matrix[r:ri, c:ci]
                    if np.sum(submatrix) == -97:
                        submatrices.append(submatrix)
    return submatrices
