
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 122 + 1):
        for j in range(matrix.shape[1] - 122 + 1):
            if np.count_nonzero(matrix[i:i+122, j:j+122]) == 122:
                count += 1
    return count
