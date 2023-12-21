
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for size in range(1, min(m, n) + 1):
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                submatrix = matrix[i:i+size, j:j+size]
                if submatrix.size == 76:
                    count += 1
    return count
