
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for row in range(nrows):
        for col in range(ncols):
            for r in range(row+1, nrows+1):
                for c in range(col+1, ncols+1):
                    submatrix = matrix[row:r, col:c]
                    if np.sum(submatrix) == 17:
                        submatrices.append(submatrix)
    return submatrices
