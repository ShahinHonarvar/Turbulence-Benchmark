
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i+1, rows+1):
                for y in range(j+1, cols+1):
                    submatrix = mat[i:x, j:y]
                    if np.sum(submatrix) == 15:
                        submatrices.append(submatrix)
    return submatrices
