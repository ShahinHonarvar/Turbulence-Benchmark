

import numpy as np

def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    nrows, ncols = matrix.shape
    for sizex in range(1, nrows+1):
        for sizey in range(1, ncols+1):
            for i in range(nrows-sizex+1):
                for j in range(ncols-sizey+1):
                    submatrix = matrix[i:i+sizex, j:j+sizey]
                    if np.sum(submatrix) == -13:
                        all_submatrices.append(submatrix)
    return all_submatrices
