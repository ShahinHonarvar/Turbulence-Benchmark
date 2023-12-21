
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 82):
        for j in range(matrix.shape[1] - 82):
            if matrix[i:i + 83, j:j + 83].sum() == 83 * 83:
                count += 1

    return count
