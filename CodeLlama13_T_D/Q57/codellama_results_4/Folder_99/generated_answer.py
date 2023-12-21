
import numpy as np
def submatrix_with_particular_sum(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n-1):
        for j in range(m-1):
            submat = mat[i:i+2,j:j+2]
            if np.sum(submat) == -185:
                return submat.tolist()
    return []
