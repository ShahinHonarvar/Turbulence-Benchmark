
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == 35:
                        submatrices.append(submatrix.tolist())
    return submatrices
