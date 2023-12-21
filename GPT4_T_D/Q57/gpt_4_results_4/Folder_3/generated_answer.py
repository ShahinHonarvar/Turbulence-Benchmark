
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    submatrices = []

    for size_i in range(1, rows+1):
        for size_j in range(1, cols+1):
            for i in range(0, rows - size_i + 1):
                for j in range(0, cols - size_j + 1):
                    submatrix = mat[i: i + size_i, j: j + size_j]
                    if np.sum(submatrix) == 54:
                        submatrices.append(submatrix)

    return submatrices
