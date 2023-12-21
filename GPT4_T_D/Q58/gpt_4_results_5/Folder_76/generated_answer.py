
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            for x in range(i, nrows):
                for y in range(j, ncols):
                    if (x-i+1)*(y-j+1) == 159:
                        count += 1
    return count
