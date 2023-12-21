
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    
    for row in range(rows):
        for col in range(cols):
            for dim in range(1, min(rows-row, cols-col)+1):
                submatrix = matrix[row:row+dim, col:col+dim]
                if np.sum(submatrix) == -82:
                    submatrices.append(submatrix)

    return submatrices
