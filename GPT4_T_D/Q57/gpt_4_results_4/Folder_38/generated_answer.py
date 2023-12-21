
import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    l = []
    for x in range(n):
        for y in range(m):
            for i in range(1, n - x + 1):
                for j in range(1, m - y + 1):
                    submatrix = matrix[x:x + i, y:y + j]
                    if np.sum(submatrix) == 34:
                        l.append(submatrix)
    return l
