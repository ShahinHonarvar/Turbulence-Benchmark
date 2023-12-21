
import numpy as np

def submatrix_with_particular_sum(mat):
    m, n = mat.shape
    for i in range(m-1):
        for j in range(n-1):
            for k in range(i+1, m):
                for l in range(j+1, n):
                    if np.sum(mat[i:k, j:l]) == 411:
                        return mat[i:k, j:l].tolist()
    return []
