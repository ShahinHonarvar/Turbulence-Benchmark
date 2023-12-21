
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for sub_matrix_i in range(i + 1, matrix.shape[0] + 1):
                for sub_matrix_j in range(j + 1, matrix.shape[1] + 1):
                    sub_matrix = matrix[i:sub_matrix_i, j:sub_matrix_j]
                    if np.sum(sub_matrix) == -137:
                        result.append(sub_matrix.tolist())
    return result
