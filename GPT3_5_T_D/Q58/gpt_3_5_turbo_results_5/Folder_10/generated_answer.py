
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 7):
        for j in range(cols - 7):
            submatrix = matrix[i:i+8, j:j+8]
            if np.sum(submatrix) == 56:
                count += 1
    return count
