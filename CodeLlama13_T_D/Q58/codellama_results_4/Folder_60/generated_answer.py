
import numpy as np

def submatrix_with_n_numbers(mat, n):
    rows, cols = mat.shape
    for i in range(rows-n+1):
        for j in range(cols-n+1):
            if all(np.array([row[j:j+n] for row in mat[i:i+n]]) == n):
                return True
    return False
