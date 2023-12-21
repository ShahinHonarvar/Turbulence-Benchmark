
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i+1, len(matrix)+1):
                for l in range(j+1, len(matrix[0])+1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == -863:
                        submatrices.append(submatrix.tolist())
    return submatrices
