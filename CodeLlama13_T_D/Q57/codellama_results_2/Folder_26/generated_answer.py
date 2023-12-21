
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    for r in range(rows):
        for c in range(cols):
            for d in range(r+1, rows+1):
                for e in range(c+1, cols+1):
                    submatrix = mat[r:d, c:e]
                    if np.sum(submatrix) == 997:
                        return [submatrix]
    return []
