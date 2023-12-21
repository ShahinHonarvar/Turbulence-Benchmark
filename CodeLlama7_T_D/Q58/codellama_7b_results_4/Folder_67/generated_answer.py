
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 3):
        for j in range(matrix.shape[1] - 3):
            if all([x == 43 for x in matrix[i:i+4, j:j+4].ravel()]):
                count += 1

    return count
