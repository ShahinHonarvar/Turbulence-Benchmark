
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    nrows, ncols = matrix.shape
    for row_num in range(1, nrows + 1):
        for col_num in range(1, ncols + 1):
            for i in range(nrows - row_num + 1):
                for j in range(ncols - col_num + 1):
                    submatrix = matrix[i: i + row_num, j: j + col_num]
                    if np.sum(submatrix) == -6:
                        submatrices.append(submatrix)
    return submatrices
