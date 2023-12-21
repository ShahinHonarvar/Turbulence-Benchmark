
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(i + 1, matrix.shape[0]):
            if sum(matrix[i]) == 20 and sum(matrix[j]) == 20:
                count += 1
    return count
