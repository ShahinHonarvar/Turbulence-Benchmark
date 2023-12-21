
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    res = []
    for i in range(nrows):
        for j in range(ncols):
            for x in range(i, nrows):
                for y in range(j, ncols):
                    submatrix = matrix[i:x+1, j:y+1]
                    if np.sum(submatrix) == 997:
                        res.append(submatrix)
    return res
