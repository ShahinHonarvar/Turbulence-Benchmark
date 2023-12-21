
import numpy as np
def submatrix_with_particular_sum(mat):
    r, c = mat.shape
    submatrices = []
    for size in range(1, min(r, c) + 1):
        for row in range(r - size + 1):
            for col in range(c - size + 1):
                submatrix = mat[row:row + size, col:col + size]
                if np.sum(submatrix) == 382:
                    submatrices.append(submatrix)
    return submatrices
