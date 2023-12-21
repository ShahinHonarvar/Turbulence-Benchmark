
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n_row, n_col = matrix.shape
    target_sum = 862
    for i in range(n_row):
        for j in range(n_col):
            for k in range(i, n_row):
                for l in range(j, n_col):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix.tolist())
    return submatrices
