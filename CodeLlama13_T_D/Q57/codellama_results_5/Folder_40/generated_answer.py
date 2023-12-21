
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i+1, rows):
                for l in range(j+1, cols):
                    if mat[i:k+1, j:l+1].sum() == -10:
                        return [mat[i:k+1, j:l+1]]
    return []
