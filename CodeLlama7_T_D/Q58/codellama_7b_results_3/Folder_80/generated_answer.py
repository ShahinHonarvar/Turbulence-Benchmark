
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 180 + 1):
        for j in range(len(matrix[0]) - 180 + 1):
            if np.sum(matrix[i:i+180, j:j+180]) == 180:
                count += 1
    return count
