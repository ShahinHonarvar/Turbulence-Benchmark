
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if np.sum(mat[i:k+1, j:l+1]) == 41:
                        return mat[i:k+1, j:l+1].tolist()
    return []
