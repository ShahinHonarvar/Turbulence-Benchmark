
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    
    for r in range(rows):
        for c in range(cols):
            for i in range(r, rows):
                for j in range(c, cols):
                    submatrix = matrix[r:i+1, c:j+1]
                    if np.sum(submatrix) == -83:
                        result.append(submatrix.tolist())
    
    return result
