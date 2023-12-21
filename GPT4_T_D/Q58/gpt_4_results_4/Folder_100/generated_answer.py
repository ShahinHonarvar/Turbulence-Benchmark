
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for x_size in range(1, m+1):
        for y_size in range(1, n+1):
            if x_size*y_size == 10:
                for x in range(m-x_size+1):
                    for y in range(n-y_size+1):
                        count += 1
    return count
