
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape[0], matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if (k-i+1)*(l-j+1) == 39:
                        count += 1
    return count
