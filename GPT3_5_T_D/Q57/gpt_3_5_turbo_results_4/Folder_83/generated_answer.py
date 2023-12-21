
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for m in range(i, len(matrix)):
                for n in range(j, len(matrix[i])):
                    submatrix = matrix[i:m+1, j:n+1]
                    if submatrix.sum() == -15:
                        submatrices.append(submatrix.tolist())
    return submatrices
