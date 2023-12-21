
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 90 + 1):
        for j in range(matrix.shape[1] - 90 + 1):
            if np.all(matrix[i:i+90, j:j+90] == 90):
                count += 1
    return count
