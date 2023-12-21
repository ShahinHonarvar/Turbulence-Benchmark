
import numpy as np

def submatrix_with_particular_sum(mat):
    n, m = mat.shape
    res = []
    
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    submat = mat[x1:x2+1, y1:y2+1]
                    if np.sum(submat) == -44:
                        res.append(submat.tolist())
    return res
