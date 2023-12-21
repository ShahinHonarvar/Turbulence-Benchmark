
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    height, width = matrix.shape
    for i in range(height - 1):
        for j in range(width - 1):
            submatrix = matrix[i:i+2, j:j+2]
            if np.sum(submatrix) == 34:
                count += 1
    return count
