
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[0], matrix.shape[1]
    result = []
    for r1 in range(0, rows):
        for r2 in range(r1+1, rows+1):
            for c1 in range(0, cols):
                for c2 in range(c1+1, cols+1):
                    submatrix = matrix[r1:r2, c1:c2]
                    if np.sum(submatrix) == 2:
                        result.append(submatrix.tolist())
    return result
