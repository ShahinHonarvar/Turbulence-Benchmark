
import numpy as np

def submatrix_with_particular_sum(mat):
    n, m = mat.shape
    for i in range(n):
        for j in range(m):
            curr_sum = 0
            for k in range(i, n):
                for l in range(j, m):
                    curr_sum += mat[k][l]
                    if curr_sum == 99:
                        return [mat[i:k+1, j:l+1]]
    return []
