
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 8):
        for j in range(matrix.shape[1] - 8):
            if (matrix[i:i+9, j:j+9] == 96).all():
                count += 1

    return count
