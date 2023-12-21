
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(i + 1, matrix.shape[0]):
            if matrix[i].sum() == 97 and matrix[j].sum() == 97:
                count += 1
    return count
