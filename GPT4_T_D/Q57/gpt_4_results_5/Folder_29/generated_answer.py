
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m, n = matrix.shape
    for ix in range(m):
        for jx in range(n):
            for kx in range(ix, m):
                for lx in range(jx, n):
                    submatrix = matrix[ix:kx+1, jx:lx+1]
                    if submatrix.sum() == 84:
                        result.append(submatrix)
    return result
