
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[j][i] == 175:
                count += 1

    return count
