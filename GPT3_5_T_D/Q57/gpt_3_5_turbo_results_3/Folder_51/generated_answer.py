
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix = matrix[r1:r2+1, c1:c2+1]
                    if np.sum(submatrix) == -46:
                        result.append(submatrix.tolist())
    
    return result
