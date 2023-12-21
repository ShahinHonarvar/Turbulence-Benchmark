
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 7):
        for j in range(matrix.shape[1] - 7):
            if np.all(matrix[i:i+8, j:j+8] == 87)):
                count += 1
    return count
