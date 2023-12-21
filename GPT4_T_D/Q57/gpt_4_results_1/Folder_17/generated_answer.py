
import numpy as np

def submatrix_with_particular_sum(mat):
    # get the size of the matrix
    rows, cols = mat.shape

    # store all the submatrices
    submatrices = []

    # generate all submatrices
    for row_length in range(1, rows + 1):
        for col_length in range(1, cols + 1):
            for row in range(rows - row_length + 1):
                for col in range(cols - col_length + 1):
                    submatrix = mat[row:row + row_length, col:col + col_length]
                    
                    # if sum of the submatrix is 398, add to submatrices
                    if np.sum(submatrix) == 398:
                       submatrices.append(submatrix)

    return submatrices
