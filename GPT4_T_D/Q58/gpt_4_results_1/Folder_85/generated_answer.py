
import numpy as np


def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0

    for x in range(m):
        for y in range(n):
            for p in range(x + 1, m + 1):
                for q in range(y + 1, n + 1):
                    submatrix = matrix[x:p, y:q]
                    if submatrix.size == 13:
                        count += 1

    return count
