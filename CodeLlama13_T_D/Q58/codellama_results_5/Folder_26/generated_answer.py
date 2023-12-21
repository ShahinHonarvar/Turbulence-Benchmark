
import numpy as np

def submatrix_with_n_numbers(mat):
    n = 115
    count = 0
    for i in range(len(mat) - n + 1):
        for j in range(len(mat[0]) - n + 1):
            if np.sum(mat[i:i+n, j:j+n]) == n * (n + 1) // 2:
                count += 1
    return count
