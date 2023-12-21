
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for top in range(0, rows):
        for bottom in range(top+1, rows+1):
            for left in range(0, cols):
                for right in range(left+1, cols+1):
                    submatrix = matrix[top:bottom, left:right]
                    if np.sum(submatrix) == 17:
                        result.append(submatrix.tolist())
    return result
