
import numpy as np

def submatrix_with_particular_sum(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    submatrices = []
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(i, n_rows):
                for l in range(j, n_cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == 64:
                        submatrices.append(submatrix.tolist())

    return submatrices
