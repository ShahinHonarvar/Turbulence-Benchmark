
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 5):
        for j in range(matrix.shape[1] - 5):
            if matrix[i:i+6, j:j+6].sum() == 66:
                count += 1

    return count
