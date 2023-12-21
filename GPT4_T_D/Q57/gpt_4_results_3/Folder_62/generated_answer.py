
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_sum_394 = []
    nrows, ncols = matrix.shape
    for row1 in range(nrows):
        for row2 in range(row1+1, nrows+1):
            for col1 in range(ncols):
                for col2 in range(col1+1, ncols+1):
                    submatrix = matrix[row1:row2, col1:col2]
                    if np.sum(submatrix) == 394:
                        submatrices_sum_394.append(submatrix)
    return submatrices_sum_394
