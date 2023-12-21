
import numpy as np

def submatrix_with_particular_sum(m):
    rows, cols = m.shape
    submatrices = []
    
    for row in range(rows):
        for col in range(cols):
            for size in range(1, min(rows-row, cols-col)+1):
                submatrix = m[row:row+size, col:col+size]
                if np.sum(submatrix) == -10:
                    submatrices.append(submatrix)
                    
    return submatrices
