
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 16):
        for j in range(matrix.shape[1] - 16):
            if all([matrix[i + k, j + l] == 17 for k in range(16) for l in range(16)])):
                count += 1

    return count
