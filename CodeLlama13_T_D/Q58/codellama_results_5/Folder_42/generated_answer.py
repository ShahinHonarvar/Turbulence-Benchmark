
import numpy as np

def submatrix_with_n_numbers(mat):
    n = 193
    count = 0
    for i in range(mat.shape[0] - n + 1):
        for j in range(mat.shape[1] - n + 1):
            submatrix = mat[i:i+n, j:j+n]
            if np.sum(submatrix == 1) == n:
                count += 1
    return count
