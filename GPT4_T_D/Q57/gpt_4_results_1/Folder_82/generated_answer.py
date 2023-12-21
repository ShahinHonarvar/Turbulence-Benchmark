
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for row in range(nrows):
        for col in range(ncols):
            for r_length in range(1,nrows-row+1):
                for c_length in range(1,ncols-col+1):
                    submatrix = matrix[row:row+r_length, col:col+c_length]
                    if np.sum(submatrix) == -27:
                        submatrices.append(submatrix.tolist())
    return submatrices
