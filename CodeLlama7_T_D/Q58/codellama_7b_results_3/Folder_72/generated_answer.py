
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 15):
        for j in range(matrix.shape[1] - 15):
            if all(matrix[i + k, j + l] == 16 for k in range(16) for l in range(16)):
                count += 1
    return count
