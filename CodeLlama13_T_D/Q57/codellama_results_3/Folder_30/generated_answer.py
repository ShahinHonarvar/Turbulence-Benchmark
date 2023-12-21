
import numpy as np
def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submat = mat[i:k+1, j:l+1]
                    if np.sum(submat) == 21:
                        return [submat]
    return []
