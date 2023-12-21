
import numpy as np

def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    rows, cols = matrix.shape

    for i in range(0, rows):
        for j in range(0, cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == -90:
                        all_submatrices.append(submatrix)

    return all_submatrices
