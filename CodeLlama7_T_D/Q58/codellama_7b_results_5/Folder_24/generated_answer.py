
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 50):
        for j in range(matrix.shape[1] - 50):
            if matrix[i:i+51, j:j+51].sum() == 51 * 51:
                count += 1

    return count
