
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for p in range(i, m):
                for q in range(j, n):
                    if (p-i+1) * (q-j+1) == 126:
                        count += 1
    return count
