
import numpy as np

def submatrix_with_n_numbers(mat):
    n = 16
    count = 0
    for i in range(len(mat) - n + 1):
        for j in range(len(mat[0]) - n + 1):
            if np.all(np.array(mat[i:i+n, j:j+n]) == n):
                count += 1
    return count
