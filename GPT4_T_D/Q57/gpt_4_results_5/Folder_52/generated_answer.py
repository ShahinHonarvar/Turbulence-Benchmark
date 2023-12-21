
import numpy as np

def submatrix_with_particular_sum(mat):
    row, col = mat.shape
    submatrices = []
    for size in range(1, min(row, col) + 1): 
        for x in range(row - size + 1):
            for y in range(col - size + 1):
                submatrix = mat[x:x+size, y:y+size]
                if np.sum(submatrix) == 100:
                    submatrices.append(submatrix)
    return submatrices
