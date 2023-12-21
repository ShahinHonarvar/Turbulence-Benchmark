
import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for row1 in range(nrows):
        for row2 in range(row1+1, nrows+1):
            for col1 in range(ncols):
                for col2 in range(col1+1, ncols+1):
                    submatrix = matrix[row1:row2, col1:col2]
                    if np.size(submatrix) == 37:
                        count += 1
    return count
