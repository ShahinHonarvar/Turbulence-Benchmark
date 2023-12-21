
import numpy as np
def submatrix_with_n_numbers(mat):
    n = 131
    cnt = 0
    for i in range(len(mat) - n + 1):
        for j in range(len(mat[0]) - n + 1):
            submat = mat[i:i+n, j:j+n]
            if np.sum(submat) == n*n:
                cnt += 1
    return cnt
