
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for i in range(r+1, rows+1):
                for j in range(c+1, cols+1):
                    submatrix = matrix[r:i, c:j]
                    if np.sum(submatrix) == 1:
                        result.append(submatrix.tolist())
    return result
