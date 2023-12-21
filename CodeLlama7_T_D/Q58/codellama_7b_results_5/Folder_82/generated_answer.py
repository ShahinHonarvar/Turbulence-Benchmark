
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 99 + 1):
        for j in range(matrix.shape[1] - 99 + 1):
            if matrix[i:i+99, j:j+99].all() == 99:
                count += 1

    return count
