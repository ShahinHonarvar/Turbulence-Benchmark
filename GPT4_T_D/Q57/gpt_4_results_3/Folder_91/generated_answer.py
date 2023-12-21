
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    for row in range(rows):
        for col in range(cols):
            for x in range(row, rows):
                for y in range(col, cols):
                    submatrix = matrix[row:x+1, col:y+1]
                    if np.sum(submatrix) == -6:
                        submatrices.append(submatrix)
                        
    return submatrices
