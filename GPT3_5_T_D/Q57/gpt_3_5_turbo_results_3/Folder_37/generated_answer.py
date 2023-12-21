
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    nrows, ncols = matrix.shape

    for row_start in range(nrows):
        for row_end in range(row_start+1, nrows+1):
            for col_start in range(ncols):
                for col_end in range(col_start+1, ncols+1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.sum(submatrix) == -82:
                        submatrices.append(submatrix.tolist())

    return submatrices
