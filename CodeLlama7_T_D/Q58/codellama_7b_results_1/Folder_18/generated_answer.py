
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 103):
        for j in range(matrix.shape[1] - 103):
            if all(matrix[i + k, j + l] == 104 for k in range(104) for l in range(104))):
                count += 1

    return count
