
import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = np.shape(matrix)
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            for k in range(2, ncols-j+1):
                for l in range(2, nrows-i+1):
                    if k*l == 20:
                        count += 1
    return count
