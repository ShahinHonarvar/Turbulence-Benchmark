
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    res = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            for k in range(m):
                for l in range(k + 1, m + 1):
                    submatrix = matrix[k:l, i:j]
                    if np.sum(submatrix) == -59:
                        res.append(submatrix)
    return res
