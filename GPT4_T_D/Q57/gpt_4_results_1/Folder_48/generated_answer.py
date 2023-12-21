
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape 
    submatrices = []
    
    for row in range(rows):
        for col in range(cols):
            for size in range(1, min(rows-row, cols-col)+1):
                submatrix = matrix[row:row+size, col:col+size]
                if np.sum(submatrix) == -261:
                    submatrices.append(submatrix)
    
    return submatrices
