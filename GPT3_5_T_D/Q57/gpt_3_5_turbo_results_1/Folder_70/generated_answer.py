
import numpy as np

def submatrix_with_particular_sum(matrix):
    def find_submatrix_sum(submatrix):
        return np.sum(submatrix) == 411

    submatrices = []
    rows, columns = matrix.shape

    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    submatrix = matrix[i:k+1, j:l+1]
                    if find_submatrix_sum(submatrix):
                        submatrices.append(submatrix.tolist())

    return submatrices
