
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    
    for r1 in range(rows):
        for r2 in range(r1 + 1, rows + 1):
            for c1 in range(cols):
                for c2 in range(c1 + 1, cols + 1):
                    submatrix = matrix[r1:r2, c1:c2]
                    if np.sum(submatrix) == 59:
                        result.append(submatrix.tolist())
    
    return result
