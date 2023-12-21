
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 4):
        for j in range(matrix.shape[1] - 4):
            if sum([matrix[i + k, j + l] for k in range(5) for l in range(5)]) == 25:
                count += 1
    return count
