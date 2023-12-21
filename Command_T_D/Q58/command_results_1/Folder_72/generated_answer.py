import numpy as np
def submatrix_with_n_numbers(matrix):
    m = len(matrix)
    n = len(matrix[0])
    return sum(
        np.where(np.sum(np.sum(matrix[i:j+1, k:l+1], axis=1) == 16, axis=0) == 1, True, False)
        for i in range(m)
        for j in range(i, m)
        for k in range(n)
        for l in range(k, n))
