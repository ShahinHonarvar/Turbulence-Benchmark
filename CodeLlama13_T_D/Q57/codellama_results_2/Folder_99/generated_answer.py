
import numpy as np
def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for r1 in range(rows-1):
        for c1 in range(cols-1):
            for r2 in range(r1+1, rows):
                for c2 in range(c1+1, cols):
                    submatrix = matrix[r1:r2+1, c1:c2+1]
                    if np.sum(submatrix) == -185:
                        return submatrix
    return []
