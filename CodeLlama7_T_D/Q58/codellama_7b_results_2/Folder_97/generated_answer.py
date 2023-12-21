
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 120 + 1):
        for j in range(matrix.shape[1] - 120 + 1):
            if matrix[i:i+120, j:j+120].sum() == 120:
                count += 1
    return count
