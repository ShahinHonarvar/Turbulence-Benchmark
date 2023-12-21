
import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for i in range(nrows):
        for j in range(ncols):
            for p in range(i+1, nrows+1):
                for q in range(j+1, ncols+1):
                    if p * q == 147:
                        count +=1
    return count
