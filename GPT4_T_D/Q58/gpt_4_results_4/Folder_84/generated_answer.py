
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for p in range(m - i + 1):
                for q in range(n - j + 1):
                    submatrix = matrix[p: p + i, q: q + j]
                    if submatrix.size == 127:
                        count += 1
    return count
