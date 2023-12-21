
import numpy as np

def submatrix_with_particular_sum(mat):
    m, n = mat.shape
    for i in range(m-1):
        for j in range(n-1):
            if np.sum(mat[i:i+2,j:j+2]) == -15:
                return [mat[i:i+2,j:j+2]]
    return []
