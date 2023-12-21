
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    for i in range(rows-3):
        for j in range(cols-3):
            submatrix = matrix[i:i+4, j:j+4]
            if np.sum(submatrix) == 45:
                return 1
    return 0
