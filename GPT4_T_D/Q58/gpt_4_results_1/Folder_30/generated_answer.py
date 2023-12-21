
import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for m in range(i, matrix.shape[0]):
                for n in range(j, matrix.shape[1]):
                    if (m+1-i) * (n+1-j) == 94:
                        submatrix_count += 1
    return submatrix_count
