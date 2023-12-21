
import numpy as np

def submatrix_with_particular_sum(matrix):

    result = []
    rows, cols = matrix.shape
    
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    submatrix = matrix[row:r + 1, col:c + 1]
                    if np.sum(submatrix) == 8:
                        result.append(submatrix.tolist())
    
    return result
