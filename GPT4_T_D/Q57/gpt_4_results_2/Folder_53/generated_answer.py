
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for r in range(i+1, rows+1):
                for c in range(j+1, cols+1):
                    submatrix = matrix[i:r, j:c]
                    if np.sum(submatrix) == -37:
                        result.append(submatrix.tolist())
    return result
