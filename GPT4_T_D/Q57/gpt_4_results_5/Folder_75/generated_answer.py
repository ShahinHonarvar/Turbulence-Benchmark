
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    nrows, ncols = matrix.shape
    for row_size in range(nrows+1):
        for col_size in range(ncols+1):
            for i in range(nrows - row_size + 1):
                for j in range(ncols - col_size + 1):
                    submatrix = matrix[i:i+row_size, j:j+col_size]
                    if np.sum(submatrix) == 16:
                        result.append(submatrix)
    return result
