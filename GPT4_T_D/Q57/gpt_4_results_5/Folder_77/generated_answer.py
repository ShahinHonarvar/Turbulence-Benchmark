
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    size = matrix.shape
    for sub_matrix_i in range(1, size[0] + 1):
        for sub_matrix_j in range(1, size[1] + 1):
            for i in range(size[0] - sub_matrix_i + 1):
                for j in range(size[1] - sub_matrix_j + 1):
                    sub_matrix = matrix[i:i+sub_matrix_i, j:j+sub_matrix_j]
                    if np.sum(sub_matrix) == -336:
                        result.append(sub_matrix)
    return result
