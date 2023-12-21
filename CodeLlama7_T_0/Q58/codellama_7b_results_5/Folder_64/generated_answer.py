
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 6):
        for j in range(matrix.shape[1] - 6):
            if matrix[i:i+7, j:j+7].sum() == 7 * 7:
                count += 1
    return count
