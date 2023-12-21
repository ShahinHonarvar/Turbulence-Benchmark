
import numpy as np

def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            current_sum = 0
            for k in range(i, i + matrix.shape[0]):
                for l in range(j, j + matrix.shape[1]):
                    if (k < matrix.shape[0]) and (l < matrix.shape[1]):
                        current_sum += matrix[k][l]
            if current_sum == 78:
                all_submatrices.append(matrix[i:i + matrix.shape[0], j:j + matrix.shape[1]]))
    return all_submatrices
