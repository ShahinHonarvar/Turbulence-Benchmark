
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m-3):
        for j in range(n-3):
            submatrix = matrix[i:i+4, j:j+4]
            if np.sum(submatrix) == 80:
                count += 1
    return count
