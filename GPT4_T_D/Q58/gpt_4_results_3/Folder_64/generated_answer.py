
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    nrows, ncols = matrix.shape
    for i in range(1, nrows+1):
        for j in range(1, ncols+1):
            for k in range(i):
                for l in range(j):
                    if ((k+1)*(l+1)) == 7:
                        count += 1
    return count
