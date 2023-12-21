
import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for p in range(i+4, m+1):
                for q in range(j+4, n+1):
                    if (p - i) * (q - j) == 16:
                        count += 1
    return count
