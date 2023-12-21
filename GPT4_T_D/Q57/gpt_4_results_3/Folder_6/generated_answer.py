
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    nrows, ncols = matrix.shape

    for row in range(0, nrows):
        for col in range(0, ncols):
            for i in range(row + 1, nrows + 1):
                for j in range(col + 1, ncols + 1):
                    submatrix = matrix[row:i, col:j]
                    if np.sum(submatrix) == 126:
                        submatrices.append(submatrix.tolist())
                
    return submatrices
