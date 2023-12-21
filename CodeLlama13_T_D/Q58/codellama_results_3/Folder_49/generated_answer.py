
import numpy as np
def submatrix_with_n_numbers(mat, n):
    rows, cols = mat.shape
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.sum(mat[i:i+n, j:j+n]) == n**2 * n:
                return 1
    return 0
