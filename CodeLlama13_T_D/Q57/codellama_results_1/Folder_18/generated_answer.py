
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            curr_sum = 0
            for k in range(i, rows):
                for l in range(j, cols):
                    curr_sum += mat[k][l]
                    if curr_sum == 616:
                        return [mat[i:k+1, j:l+1]]
    return []
