
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 8):
        for j in range(matrix.shape[1] - 8):
            if all([matrix[i + k][j + l] == 9 for k in range(9) for l in range(9)])):
                count += 1
    return count
