
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 76 + 1):
        for j in range(matrix.shape[1] - 76 + 1):
            if np.count_nonzero(matrix[i:i+76, j:j+76]) == 76:
                count += 1
    return count
