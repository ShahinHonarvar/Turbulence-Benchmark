
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 3):
        for j in range(matrix.shape[1] - 3):
            if all([matrix[i + k, j + l] == 43 for k in range(3) for l in range(3)])):
                count += 1

    return count
