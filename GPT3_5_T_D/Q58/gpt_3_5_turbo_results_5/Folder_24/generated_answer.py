
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 50):
        for j in range(len(matrix[0]) - 50):
            submatrix = matrix[i:i+51, j:j+51]
            if np.sum(submatrix) == 51 * 51:
                count += 1
    return count
