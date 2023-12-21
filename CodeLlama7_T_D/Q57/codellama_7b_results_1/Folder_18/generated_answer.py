
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if sum(matrix[i:i+2, j:j+2]) == 616:
                submatrices.append(matrix[i:i+2, j:j+2])
    return submatrices
