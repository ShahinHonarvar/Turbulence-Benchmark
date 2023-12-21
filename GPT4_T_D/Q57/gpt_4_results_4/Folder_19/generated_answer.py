
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[0], matrix.shape[1]
    submatrices = []

    for i in range(0, rows):
        for j in range(0, cols):
            for r in range(i+1, rows+1):
                for c in range(j+1, cols+1):
                    submatrix = matrix[i:r, j:c]
                    if np.sum(submatrix) == -97:
                        submatrices.append(submatrix)
    return submatrices
