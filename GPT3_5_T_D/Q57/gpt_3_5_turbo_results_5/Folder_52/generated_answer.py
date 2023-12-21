
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    
    for top in range(rows):
        for bottom in range(top + 1, rows + 1):
            for left in range(cols):
                for right in range(left + 1, cols + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if submatrix.sum() == 100:
                        result.append(submatrix.tolist())
    
    return result
