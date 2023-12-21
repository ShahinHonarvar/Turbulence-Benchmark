
import numpy as np
def submatrix_with_n_numbers(mat):
    n = 191
    rows, cols = mat.shape
    count = 0
    for i in range(rows-n+1):
        for j in range(cols-n+1):
            submat = mat[i:i+n,j:j+n]
            if np.sum(submat) == n*n:
                count += 1
    return count
