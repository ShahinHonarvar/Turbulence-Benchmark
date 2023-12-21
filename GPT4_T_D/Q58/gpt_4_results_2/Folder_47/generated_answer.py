
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for r in range(nrows):
        for c in range(ncols):
            for i in range(r, nrows):
                for j in range(c, ncols):
                    submatrix = matrix[r:i + 1, c:j + 1]
                    if np.size(submatrix) == 90:
                        count += 1
    return count
