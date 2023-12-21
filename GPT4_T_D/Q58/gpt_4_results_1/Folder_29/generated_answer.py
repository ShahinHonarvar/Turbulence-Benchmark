
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for a in range(i, n + 1):
                for b in range(j, m + 1):
                    if ((a - i + 1) * (b - j + 1)) == 19:
                        count += 1
    return count
