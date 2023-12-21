
import numpy as np

def submatrix_with_particular_sum(matrix):
    row, col = matrix.shape
    result = []

    for r1 in range(row):
        for c1 in range(col):
            for r2 in range(r1, row):
                for c2 in range(c1, col):
                    submatrix = matrix[r1:r2+1, c1:c2+1]
                    if np.sum(submatrix) == -20:
                        result.append(submatrix)
    
    return result
