
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for row in range(nrows):
        for col in range(ncols):
            for x in range(row, nrows):
                for y in range(col, ncols):
                    submatrix = matrix[row:x+1, col:y+1]
                    if np.sum(submatrix) == -25:
                        result.append(submatrix)
    return result
