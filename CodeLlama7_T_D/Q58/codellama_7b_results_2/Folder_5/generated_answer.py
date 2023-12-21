
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 63):
        for j in range(matrix.shape[1] - 63):
            if sum(matrix[i:i+63, j:j+63].flatten()) == 63:
                count += 1

    return count
