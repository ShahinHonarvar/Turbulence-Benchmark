
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = np.shape(matrix)
    for a in range(m):
        for b in range(n):
            for c in range(a+1, m+1):
                for d in range(b+1, n+1):
                    if (c-a)*(d-b) == 103:
                        count += 1
    return count
