
import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    sub_matrix = matrix[i:x+1, j:y+1]
                    if np.sum(sub_matrix) == 398:
                        sub_matrices.append(sub_matrix)
    return sub_matrices
