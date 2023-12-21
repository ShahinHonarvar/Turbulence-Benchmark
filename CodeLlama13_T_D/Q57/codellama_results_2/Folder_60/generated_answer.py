
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i+1, rows):
                for l in range(j+1, cols):
                    submatrix = mat[i:k, j:l]
                    if np.sum(submatrix) == 94:
                        return [submatrix]
    return []
