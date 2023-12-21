
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    submatrices = []
    for size in range(1, min(nrows, ncols) + 1):
        for i in range(nrows - size + 1):
            for j in range(ncols - size + 1):
                submatrix = matrix[i:i+size, j:j+size]
                if np.sum(submatrix) == -128:
                    submatrices.append(submatrix)
    return submatrices
