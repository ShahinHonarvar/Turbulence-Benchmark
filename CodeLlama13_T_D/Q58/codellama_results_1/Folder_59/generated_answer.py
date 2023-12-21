
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    rows, cols = matrix.shape
    for i in range(rows-n+1):
        for j in range(cols-n+1):
            submatrix = matrix[i:i+n, j:j+n]
            if np.sum(submatrix) == n*76:
                return 1
    return 0
