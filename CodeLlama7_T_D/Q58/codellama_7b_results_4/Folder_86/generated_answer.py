
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 137):
        for j in range(matrix.shape[1] - 137):
            if all([matrix[i + k][j + l] == 138 for k in range(138) for l in range(138)])):
                count += 1
    return count
