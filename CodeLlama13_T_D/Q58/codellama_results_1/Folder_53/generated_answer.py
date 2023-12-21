
import numpy as np
def submatrix_with_n_numbers(matrix):
    n = 24
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(set(matrix[i][j:j+n])) == n:
                count += 1
    return count
