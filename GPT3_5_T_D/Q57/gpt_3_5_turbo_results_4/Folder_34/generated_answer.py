
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    nrows, ncols = matrix.shape

    for r in range(nrows):
        for c in range(ncols):
            for i in range(r, nrows):
                for j in range(c, ncols):
                    submatrix = matrix[r:i+1, c:j+1]
                    if np.sum(submatrix) == -13:
                        submatrices.append(submatrix.tolist())

    return submatrices
