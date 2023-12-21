
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 120):
        for j in range(matrix.shape[1] - 120):
            if np.all(matrix[i:i+120, j:j+120] == 121):
                count += 1
    return count
