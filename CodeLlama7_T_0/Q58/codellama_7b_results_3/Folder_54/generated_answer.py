
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 26):
        for j in range(matrix.shape[1] - 26):
            if all(matrix[i + k, j + l] == 27 for k in range(27) for l in range(27))):
                count += 1
    return count
