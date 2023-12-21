
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.size(submatrix) == 179:
                        count += 1
    return count
