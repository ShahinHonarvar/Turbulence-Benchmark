
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    nrows, ncols = matrix.shape
    for row in range(nrows):
        for col in range(ncols):
            for x in range(row+1, nrows+1):
                for y in range(col+1, ncols+1):
                    submatrix = matrix[row:x, col:y]
                    if np.sum(submatrix) == -308:
                        result.append(submatrix)
    return result
