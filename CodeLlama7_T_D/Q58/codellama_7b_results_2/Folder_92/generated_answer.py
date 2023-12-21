
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 8 + 1):
        for j in range(matrix.shape[1] - 8 + 1):
            if sum(matrix[i:i+8, j:j+8]) == 8 * 8:
                count += 1

    return count
