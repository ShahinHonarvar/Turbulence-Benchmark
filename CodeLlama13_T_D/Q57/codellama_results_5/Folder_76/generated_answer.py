
import numpy as np
def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            curr_row = mat[i]
            curr_col = mat[:,j]
            for k in range(1, rows-i+1):
                for l in range(1, cols-j+1):
                    submat = mat[i:i+k, j:j+l]
                    if np.sum(submat) == -255:
                        return [submat]
    return []
