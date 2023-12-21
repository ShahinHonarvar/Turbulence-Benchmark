
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows):
                for l in range(j, num_cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == -77:
                        submatrices.append(submatrix.tolist())

    return submatrices
