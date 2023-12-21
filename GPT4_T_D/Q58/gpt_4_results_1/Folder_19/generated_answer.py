
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    if (k-i+1)*(l-j+1) == 17:
                        count += 1
    return count
