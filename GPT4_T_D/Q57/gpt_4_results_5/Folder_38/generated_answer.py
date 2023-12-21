
import numpy as np

def submatrix_with_particular_sum(mat):
    nrows, ncols = mat.shape

    submatrices = []

    for row1 in range(nrows):
        for row2 in range(row1 + 1, nrows + 1):
            for col1 in range(ncols):
                for col2 in range(col1 + 1, ncols + 1):

                    submatrix = mat[row1:row2, col1:col2]
                    if submatrix.sum() == 34:
                        submatrices.append(submatrix)
    
    return submatrices
