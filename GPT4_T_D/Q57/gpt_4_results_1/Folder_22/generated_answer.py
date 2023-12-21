
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submatrix = mat[i:x+1, j:y+1]
                    if submatrix.sum() == -38:
                        submatrices.append(submatrix)
    return submatrices
