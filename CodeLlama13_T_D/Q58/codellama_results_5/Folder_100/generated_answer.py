
import numpy as np

def submatrix_with_n_numbers(mat):
    n = 10
    count = 0
    for i in range(len(mat) - n + 1):
        for j in range(len(mat[0]) - n + 1):
            submat = mat[i:i+n, j:j+n]
            if np.sum(submat == 1) == n:
                count += 1
    return count
