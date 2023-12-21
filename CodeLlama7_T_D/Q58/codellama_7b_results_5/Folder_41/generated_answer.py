
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 73 + 1):
        for j in range(matrix.shape[1] - 73 + 1):
            if all([matrix[i + k, j + l] == 73 for k in range(73) for l in range(73)])):
                count += 1
    return count
