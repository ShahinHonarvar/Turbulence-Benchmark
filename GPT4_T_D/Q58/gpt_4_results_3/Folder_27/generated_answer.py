
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            for k in range(i+1, r+1):
                for l in range(j+1, c+1):
                    if (k-i)*(l-j) == 77:
                        count += 1
    return count
