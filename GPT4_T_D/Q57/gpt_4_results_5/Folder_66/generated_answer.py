
import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    nrows, ncols = matrix.shape

    for row_start in range(nrows):
        for col_start in range(ncols):
            for row_end in range(row_start, nrows):
                for col_end in range(col_start, ncols):
                    submatrix = matrix[row_start:row_end+1, col_start:col_end+1]
                    if submatrix.sum() == 99:
                        list_of_submatrices.append(submatrix)
    return list_of_submatrices
