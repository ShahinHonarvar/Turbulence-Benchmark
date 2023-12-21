
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]+1):
                for l in range(j, matrix.shape[1]+1):
                    if (k-i)*(l-j) == 85:
                        count += 1
    return count
