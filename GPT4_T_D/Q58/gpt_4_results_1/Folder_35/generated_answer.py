
import numpy as np

def submatrix_with_n_numbers(matrix):

    rows, cols = matrix.shape
    counter = 0
    
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if (m-i)*(n-j) == 111:
                        counter += 1
    return counter
