
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    rows, cols = matrix.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            submat = matrix[i:i+3, j:j+3]
            if np.count_nonzero(submat == n) == 9:
                return True
    return False
