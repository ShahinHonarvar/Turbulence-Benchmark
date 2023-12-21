
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for x in range(i, n):
                for y in range(j, m):
                    if (x - i + 1) * (y - j + 1) == 180:
                        count += 1
    return count
