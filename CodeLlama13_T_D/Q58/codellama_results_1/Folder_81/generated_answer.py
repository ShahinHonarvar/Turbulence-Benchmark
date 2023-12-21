
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    rows, cols = matrix.shape
    for i in range(rows-n+1):
        for j in range(cols-n+1):
            submat = matrix[i:i+n, j:j+n]
            if np.all(submat == 97):
                return True
    return False
