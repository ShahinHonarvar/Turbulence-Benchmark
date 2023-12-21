
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0

    for i in range(m):
        for j in range(n):
            if i + 1 < m and j + 1 < n:
                submatrix = matrix[i:i+2, j:j+2]
                if np.prod(submatrix.shape) == 8:
                    count += 1

    return count
