
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 118 + 1):
        for j in range(matrix.shape[1] - 118 + 1):
            if np.sum(matrix[i:i+118, j:j+118]) == 118 * 118:
                count += 1
    return count
