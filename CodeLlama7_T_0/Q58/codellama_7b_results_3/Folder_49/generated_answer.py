
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 72 + 1):
        for j in range(matrix.shape[1] - 72 + 1):
            if np.count_nonzero(matrix[i:i+72, j:j+72]) == 72:
                count += 1
    return count
