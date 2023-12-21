
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 7):
        for j in range(matrix.shape[1] - 7):
            if all([matrix[i + k, j + l] == 8 for k in range(8) for l in range(8)])):
                count += 1

    return count
