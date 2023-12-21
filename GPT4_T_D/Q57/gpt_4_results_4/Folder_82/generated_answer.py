
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    
    for x1 in range(rows):
        for x2 in range(x1+1, rows+1):
            for y1 in range(cols):
                for y2 in range(y1+1, cols+1):
                    submatrix = matrix[x1:x2, y1:y2]
                    if np.sum(submatrix) == -27:
                        result.append(submatrix)
    
    return result
