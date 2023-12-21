
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == 93:
                        submatrices.append(submatrix.tolist())
    return submatrices
