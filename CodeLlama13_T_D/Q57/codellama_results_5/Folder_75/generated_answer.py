
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            sum = 0
            for k in range(i, rows):
                for l in range(j, cols):
                    sum += mat[k][l]
                if sum == 16:
                    return list(mat[i:k+1, j:l+1])
    return []
