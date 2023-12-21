
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 185):
        for j in range(matrix.shape[1] - 185):
            if np.sum(matrix[i:i+186, j:j+186]) == 186:
                count += 1
    return count
