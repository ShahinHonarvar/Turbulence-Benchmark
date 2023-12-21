
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 165):
        for j in range(matrix.shape[1] - 165):
            if matrix[i:i+165, j:j+165].sum() == 176:
                count += 1
    return count
